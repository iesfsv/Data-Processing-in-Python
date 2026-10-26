## Cheat sheet: matplotlib and seaborn

### Matplotlib

**Basic pattern**
```python
fig, ax = plt.subplots()      # create the figure and one axes
ax.plot(x, y)                 # draw on the axes
ax.set_title("Title")         # decorate the axes
plt.show()                    # display
```
More options: `plt.subplots(1, 2, figsize=(10, 4))` (two panels side by side), `fig.savefig("plot.png", dpi=150)` (save).

**Plot types** (methods of `ax`)

| Method | Plot | Use for |
|---|---|---|
| `ax.plot(x, y)` | Line | Time series |
| `ax.scatter(x, y)` | Scatter | Relationship between two variables |
| `ax.bar(x, height)` | Vertical bars | Compare categories |
| `ax.barh(y, width)` | Horizontal bars | Compare categories with long names |
| `ax.hist(data, bins=30)` | Histogram | Distribution of one variable |
| `ax.boxplot(data)` | Box plot | Distribution and outliers |
| `ax.fill_between(x, y1, y2)` | Shaded area | Ranges, confidence bands |

**Decorating the plot**

| Method | What it does |
|---|---|
| `ax.set_title("...")` | Title |
| `ax.set_xlabel("...")`, `ax.set_ylabel("...")` | Axis labels |
| `ax.legend()` | Legend (only shows lines that have `label=`) |
| `ax.set_xlim(a, b)`, `ax.set_ylim(a, b)` | Axis range |
| `ax.grid(True)` | Grid lines |
| `ax.axhline(y)`, `ax.axvline(x)` | Horizontal / vertical reference line |
| `ax.text(x, y, "...")`, `ax.annotate(...)` | Text on the plot |
| `ax.tick_params(axis="y", labelcolor="green")` | Tick style |
| `ax2 = ax.twinx()` | Second y-axis (shares the x-axis) |

**Common arguments**
`label=` (legend name), `color=`, `linestyle="--"`, `linewidth=`, `marker="o"`, `alpha=` (transparency), `bins=`, `edgecolor=`, `width=` (bar width), `s=` (scatter point size)

---

### Seaborn

Seaborn draws on the same `ax`. Always pass `ax=ax`, and you can still use all the matplotlib methods afterwards.

```python
fig, ax = plt.subplots()
sns.barplot(data=df, x="species", y="body_mass_g", ax=ax)
ax.set_title("Body mass by species")   # matplotlib finishes the job
plt.show()
```

**Common arguments:** `data=` (DataFrame), `x=`, `y=`, `hue=` (colour by a category), `ax=`

| Function | Plot | Note |
|---|---|---|
| `sns.scatterplot` | Scatter | `hue=` colours by group |
| `sns.lineplot` | Line | Averages and a CI band if x has repeated values |
| `sns.barplot` | Bars | Shows the **mean** with a confidence interval |
| `sns.countplot` | Bars | Counts rows per category |
| `sns.histplot` | Histogram | `kde=True` adds a smooth curve |
| `sns.boxplot`, `sns.violinplot` | Distribution per group | Compare groups |
| `sns.heatmap` | Coloured matrix | Needs a matrix, so `pivot` first |
| `sns.regplot` | Scatter and fitted line | Quick trend |

**Heatmap arguments:** `annot=True` (numbers in cells), `fmt="d"` (number format), `cmap="YlOrRd"` (colours), `vmin`/`vmax` (colour range), `center=0` (for correlations), `linewidths=`

**Figure-level functions** (`pairplot`, `lmplot`, `relplot`, `displot`, `catplot`) create their own figure and **do not take `ax=`**.

**Other:** `sns.load_dataset("name")` loads built-in data, `sns.set_theme()` sets a nicer default style.

---

### Pandas helpers you will need for plotting

| Method | What it does |
|---|---|
| `df.head()`, `df.dtypes`, `df.isna().sum()` | Look at the data first |
| `df.dropna()` | Drop rows with missing values |
| `df.set_index("col")` | Use a column as the index (e.g. time) |
| `df[df["year"] == 2007]` | Filter rows |
| `df.groupby("col")["y"].mean()` | Average per group |
| `df.pivot(index=, columns=, values=)` | Long table to matrix (for heatmaps) |
