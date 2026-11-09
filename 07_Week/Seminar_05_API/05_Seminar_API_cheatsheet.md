# Cheatsheet: APIs (JSON) and Web Scraping (HTML)

## 0. Setup
```python
%pip install pandas requests beautifulsoup4     # run once (in a notebook cell)

import pandas as pd
import requests
from bs4 import BeautifulSoup
```

---

## 1. Python basics for JSON

JSON data is a mix of **lists** (`[...]`, indexed by number) and **dictionaries** (`{...}`, indexed by key).

| Code | What it does |
|---|---|
| `type(x)` | Type of an object (`list`, `dict`, `str`, ...) |
| `len(x)` | Number of elements (list items / dict keys / characters) |
| `my_list[0]` | First element of a list (counting starts at 0) |
| `my_list[-1]` | Last element of a list |
| `my_list[1:3]` | Slice: elements at positions 1 and 2 |
| `my_dict["key"]` | Value stored under a key (error if the key is missing) |
| `my_dict.get("key")` | Same, but returns `None` instead of an error if missing |
| `my_dict.keys()` | All keys |
| `my_dict.values()` | All values |
| `my_dict.items()` | All `(key, value)` pairs |
| `data[1][0]["country"]["value"]` | Chaining: list → list → dict → dict |

```python
for obs in data[1]:                  # loop over a list
    print(obs["date"], obs["value"])

for key, value in my_dict.items():   # loop over a dict
    print(key, value)

rows = [{"a": o["date"]} for o in data[1]]   # list comprehension (short loop)
```

---

## 2. `requests`: talking to a server

| Code | What it does |
|---|---|
| `requests.get(url)` | Download a URL, returns a `Response` object |
| `requests.get(url, params={...})` | Same, with query parameters added to the URL (`?a=1&b=2`) |
| `requests.get(url, headers={...})` | Same, with extra headers (e.g. `{"User-Agent": "Mozilla/5.0"}`) |
| `response.status_code` | Status number: `200` = OK, `404` = not found, `403` = forbidden |
| `response.ok` | `True` if the status code is below 400 |
| `response.raise_for_status()` | Raise an error if the request failed |
| `response.url` | The final URL that was requested |
| `response.text` | Body as a string (use for HTML) |
| `response.content` | Body as raw bytes (useful if the text looks garbled) |
| `response.json()` | Convert a JSON body into Python lists and dicts |
| `response.headers` | Response headers (a dict-like object) |
| `response.encoding` | Encoding used for `.text` (can be changed: `response.encoding = "utf-8"`) |

```python
response = requests.get(url, params=params)
print(response.status_code)      # always check it first
data = response.json()           # method: needs brackets
html = response.text             # attribute: no brackets
```

---

## 3. `BeautifulSoup`: reading HTML

HTML is a tree of tags: `<tag attribute="value">text</tag>`.
Use the browser **Inspect** tool (right-click → Inspect) to find the tag, `id` and `class` you need.

### Create and look at the soup
| Code | What it does |
|---|---|
| `BeautifulSoup(html, "html.parser")` | Parse an HTML string into a soup object |
| `soup.prettify()` | Re-indent the HTML so it is readable (returns a string) |
| `soup.title` | The first `<title>` tag |

### Find tags
| Code | What it does |
|---|---|
| `soup.find("ul", id="speechIndex")` | First tag that matches, or `None` |
| `soup.find("div", class_="title")` | Filter by class (note the underscore: `class_`) |
| `soup.find_all("li")` | **List** of all matching tags |
| `soup.find_all("li", limit=5)` | Only the first 5 matches |
| `tag.find(...)` / `tag.find_all(...)` | Search only **inside** one tag |
| `soup.select("ul#speechIndex li")` | Find all with a CSS selector (`#id`, `.class`, `tag tag`) |
| `soup.select_one("div.title a")` | First match of a CSS selector |

### Get data out of a tag
| Code | What it does |
|---|---|
| `tag.get_text()` | All text inside the tag (and its children) |
| `tag.get_text(strip=True)` | Same, with surrounding whitespace removed |
| `tag.text` | Shortcut for `get_text()` |
| `tag.get("href")` or `tag["href"]` | Value of an attribute (e.g. the link of an `<a>`) |
| `tag.attrs` | All attributes as a dict |
| `tag.name` | Name of the tag (`"li"`, `"div"`, ...) |
| `tag.contents` | List of the tag's children (text pieces and tags) |
| `tag.parent` | The tag one level up |
| `tag.find_next_sibling("div")` | The next tag on the same level |

```python
speech_list = soup.find("ul", id="speechIndex")
speeches = speech_list.find_all("li")

first = speeches[0]
date  = first.contents[0].strip()                              # plain text before the first child tag
title = first.find("div", class_="title").get_text(strip=True)
link  = first.find("a")["href"]
```

> `find` returns `None` if nothing matches, and then `.get_text()` fails with
> `AttributeError: 'NoneType' ...`. If you see this, your tag or class name is wrong.

---

## 4. Text cleaning (`str` methods)
| Code | What it does |
|---|---|
| `s.strip()` | Remove spaces and new lines from both ends |
| `s.split(",")` | Split a string into a list |
| `s.replace("a", "b")` | Replace text |
| `s.lower()` / `s.upper()` | Change case |
| `s.startswith("At the")` | `True` / `False` |
| `f"{name}: {value}"` | f-string: put variables into text |

---

## 5. `pandas`: collecting the results
| Code | What it does |
|---|---|
| `pd.DataFrame(rows)` | Table from a **list of dictionaries** (keys become columns) |
| `df.head(n)` / `df.tail(n)` | First / last `n` rows |
| `df.shape` | `(rows, columns)` |
| `df.columns` | Column names |
| `df.info()` | Column types and missing values |
| `df["col"]` | One column |
| `df["date"] = pd.to_datetime(df["date"])` | Convert text to real dates |
| `df["value"] = df["value"].astype(float)` | Change a column type |
| `df.sort_values("date")` | Sort rows |
| `df.to_csv("file.csv", index=False)` | Save to a CSV file |

**The standard pattern:** loop → build a list of dicts → make a DataFrame.
```python
rows = []
for li in speeches:
    rows.append({
        "title":    li.find("div", class_="title").get_text(strip=True),
        "date":     li.contents[0].strip(),
        "speaker":  li.find("div", class_="speaker").get_text(strip=True),
        "location": li.find("div", class_="location").get_text(strip=True),
    })
df = pd.DataFrame(rows)
```

---

## 6. Reading a saved HTML file (optional)
```python
from pathlib import Path
soup = BeautifulSoup(Path("page.html").read_bytes(), "html.parser")   # bytes: BeautifulSoup detects the encoding
```
`read_text(encoding="utf-8")` fails with `UnicodeDecodeError` if the file uses another encoding. Read bytes instead.

---

## 7. Common errors
| Error | Likely cause |
|---|---|
| `KeyError: 'value'` | Wrong key name, or you are one level too high or low in the nesting |
| `TypeError: list indices must be integers` | You used a key on a list (or a number on a dict) |
| `AttributeError: 'NoneType' has no attribute ...` | `find()` found nothing: check tag, `id`, `class_` |
| `status_code` 403 / 404 | Blocked or wrong URL: check the link, try a `User-Agent` header |
| `JSONDecodeError` | The response is not JSON: print `response.text[:200]` to see what you got |
| `FeatureNotFound` | Parser name not installed: use `"html.parser"` |
