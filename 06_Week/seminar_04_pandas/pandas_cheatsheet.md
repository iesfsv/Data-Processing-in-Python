# Pandas Cheatsheet (Seminar: EDA in Python)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

## 1. Loading & first look

| Task | Code |
|---|---|
| Read CSV | `df = pd.read_csv("file.csv")` |
| First / last rows | `df.head()` / `df.tail()` (default 5, or `df.head(10)`) |
| Shape (rows, cols) | `df.shape` |
| Column names | `df.columns` |
| Data types | `df.dtypes` |
| Summary stats | `df.describe()` |
| Random sample | `df.sample(10)` |

## 2. Selecting

| Task | Code |
|---|---|
| One column (Series) | `df["col"]` |
| Several columns (DataFrame) | `df[["a", "b"]]` |
| Slicing a Series | `df.dtypes[-10:]` (last 10) |
| Loop over index + value | `for name, val in df.dtypes.items(): ...` |
| Columns by type | `df.select_dtypes(include="number")` |
| Columns by your own rule | `quant = [c for c in df.columns if df.dtypes[c] != "str"]` then `df[quant]` |

> Looping directly over a Series (`for x in df.dtypes`) gives only **values**. Use `.items()` to get **index and value**.
> Note: string columns show as `str` in pandas 3.x, but as `object` in older versions.

## 3. Counting & distributions

```python
df["col"].value_counts()                    # counts per category
df["col"].value_counts(ascending=True)      # sorted ascending
df["col"].hist()                            # histogram
```

## 4. Missing data

```python
df.isna()                                   # True/False table
df.isna().sum()                             # NaNs per column
df.isna().sum().sort_values()[-20:]         # 20 columns with most NaNs
miss = df.isna().sum()
miss = miss[miss > 0]                       # keep only columns with NaNs
miss.sort_values()[-10:].plot.bar()         # bar chart of top 10
```

## 5. Filtering (boolean masks)

```python
df[df["SalePrice"] < 200000]                                  # one condition
df[(df["a"] < 5) & (df["b"] == "x")]                          # AND
df[(df["a"] < 5) | (df["b"] == "x")]                          # OR
df[df["1st Flr SF"] > df["2nd Flr SF"]]                       # compare columns
```

> Always wrap each condition in **parentheses**, and use `&`, `|` (not `and`, `or`).

## 6. Aggregation (`groupby`)

```python
df.groupby("Street")["SalePrice"].mean()                      # mean per group
df.groupby("Overall Qual")["SalePrice"].mean().plot()         # aggregate + plot
df.groupby("Overall Qual")[["SalePrice", "Overall Cond"]].agg(["mean", "max", "min"])
df[df["Street"] == "Grvl"].groupby("Street")["SalePrice"].mean()   # filter, then group
```

Pattern: **`df.groupby(group_col)[value_cols].function()`**

## 7. Dates

```python
df["date"] = pd.to_datetime(df["date"])                       # string -> datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")      # bad values -> NaT
df = df.set_index("date")                                     # date as index
pd.date_range("2025-01-31", periods=24, freq="ME")            # make a date index
```

### Resampling (needs a datetime index)

```python
m.resample("QE").sum()      # quarterly, sum
m.resample("YE").mean()     # yearly, mean
```

| Freq | Meaning |
|---|---|
| `"D"` | day |
| `"W"` | week |
| `"ME"` | month end |
| `"QE"` | quarter end |
| `"YE"` | year end |

> Older pandas used `"M"`, `"Q"`, `"Y"`. Pandas 2.2+ uses `"ME"`, `"QE"`, `"YE"`.

## 8. Quick tips

- Check types with `type(obj)`: a `DataFrame` and a `Series` behave differently in loops.
- `df.col` and `df["col"]` both work, but use brackets when names contain spaces.
- Methods return a **new** object. Assign it back (`df = ...`) to keep the change.
- Plot straight from pandas: `.plot()`, `.plot.bar()`, `.hist()`.
