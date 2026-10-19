# NumPy cheat sheet

`import numpy as np`

## Creating arrays

| Function | What it does |
|---|---|
| `np.array(list)` | array from a (nested) list |
| `np.zeros(shape)` / `np.ones(shape)` | array filled with 0 / 1 |
| `np.full(shape, val)` | array filled with `val` |
| `np.eye(n)` | identity matrix |
| `np.diag(v)` | diagonal matrix from a vector (or the diagonal of a matrix) |
| `np.arange(start, stop, step)` | evenly spaced values, `stop` excluded |
| `np.linspace(a, b, num)` | `num` evenly spaced points, `b` included |
| `np.zeros_like(a)` / `np.ones_like(a)` | zeros / ones with the shape of `a` |
| `np.empty(shape)` | uninitialised array (arbitrary values) |

## Random numbers

| Function | What it does |
|---|---|
| `rng = np.random.default_rng(seed)` | create a reproducible random generator |
| `rng.random(shape)` | uniform on [0, 1) |
| `rng.uniform(a, b, size)` | uniform on [a, b) |
| `rng.standard_normal(shape)` | N(0, 1) |
| `rng.normal(mu, sigma, size)` | N(mu, sigma²) |
| `rng.multivariate_normal(mean, cov, size)` | correlated normal draws |
| `rng.integers(low, high, size)` | random integers, `high` excluded |
| `rng.choice(a, size, replace=False)` | random sample from `a` |
| `rng.permutation(n)` | shuffled `0..n-1` (or shuffled copy of an array) |
| `rng.shuffle(a)` | shuffle `a` in place |

## Array info and types

| Function | What it does |
|---|---|
| `a.shape` / `a.ndim` / `a.size` | dimensions / number of axes / number of elements |
| `a.dtype` | data type (`float64`, `float32`, `int64`, `bool`) |
| `a.astype(np.float32)` | convert the type (returns a copy) |
| `a.copy()` | independent copy |
| `len(a)` | length of the first axis |

## Indexing and slicing

| Syntax | What it does |
|---|---|
| `a[i, j]` | single element |
| `a[i]` / `a[:, j]` | row `i` / column `j` |
| `a[i:j, k:l]` | sub-array (a view) |
| `a[::-1]` | reverse along an axis |
| `a[..., -1]` | last entry along the last axis |
| `a[mask]` | elements where the boolean `mask` is True |
| `a[mask] = val` | assign to the selected elements |
| `a[[0, 2]]` | pick rows 0 and 2 (fancy indexing, copy) |
| `a[np.ix_(rows, cols)]` | sub-grid of chosen rows and columns |
| `a[:, None]` / `a[None, :]` | add an axis (column / row vector) |

## Reshaping

| Function | What it does |
|---|---|
| `a.reshape(r, c)` | new shape, `-1` means "infer this size" |
| `a.ravel()` / `a.flatten()` | flatten to 1D (view if possible / always a copy) |
| `a.T` | transpose |
| `np.transpose(a, axes)` | permute axes in any order |
| `np.swapaxes(a, i, j)` | swap two axes |
| `np.moveaxis(a, src, dst)` | move an axis to a new position |
| `np.expand_dims(a, axis)` | insert an axis of length 1 |
| `np.squeeze(a)` | remove axes of length 1 |

## Combining and splitting

| Function | What it does |
|---|---|
| `np.concatenate([a, b], axis)` | join along an existing axis |
| `np.stack([a, b], axis)` | join along a new axis |
| `np.vstack` / `np.hstack` | stack vertically / horizontally |
| `np.c_[a, b]` | stack 1D arrays as columns |
| `np.split(a, k)` / `np.array_split(a, k)` | split into `k` parts (equal / allows unequal) |
| `np.tile(a, reps)` | repeat the whole array |
| `np.repeat(a, reps)` | repeat each element |
| `np.pad(a, width)` | add a border (zeros by default) |
| `np.flip(a)` | reverse the order |
| `np.roll(a, k)` | circular shift by `k` |

## Element-wise math

| Function | What it does |
|---|---|
| `np.exp` / `np.log` / `np.log1p` | eˣ / natural log / log(1 + x) |
| `np.sqrt` / `np.power(a, p)` / `a ** p` | square root / power |
| `np.abs` / `np.sign` | absolute value / sign |
| `np.round(a, k)` / `np.floor` / `np.ceil` | rounding |
| `np.clip(a, lo, hi)` | limit values to `[lo, hi]` |
| `np.maximum(a, b)` / `np.minimum(a, b)` | element-wise max / min |
| `np.tanh` / `np.sin` / `np.cos` | trigonometric functions |
| `np.isnan` / `np.isfinite` | test for NaN / finite values |
| `np.nan_to_num(a)` | replace NaN and inf with numbers |
| `np.diff(a)` | differences between neighbours |
| `np.cumsum(a)` / `np.cumprod(a)` | cumulative sum / product |

## Statistics and aggregation

`axis=0` collapses rows (one result per column), `axis=1` collapses columns (one result per row), `keepdims=True` keeps the axis for broadcasting.

| Function | What it does |
|---|---|
| `a.sum()` / `a.prod()` | sum / product |
| `a.mean()` / `np.average(a, weights=w)` | mean / weighted mean |
| `a.std(ddof=1)` / `a.var(ddof=1)` | sample std / variance (default `ddof=0`) |
| `a.min()` / `a.max()` | minimum / maximum |
| `a.argmin()` / `a.argmax()` | index of the minimum / maximum |
| `np.median(a)` | median |
| `np.percentile(a, q)` / `np.quantile(a, q)` | percentile (0–100) / quantile (0–1) |
| `np.cov(X, rowvar=False)` | covariance matrix (rows = observations) |
| `np.corrcoef(X, rowvar=False)` | correlation matrix |
| `np.nanmean` / `np.nansum` / `np.nanstd` | same statistics, ignoring NaN |

## Comparison and logic

| Function | What it does |
|---|---|
| `np.where(cond, x, y)` | `x` where `cond` is True, otherwise `y` |
| `np.where(cond)` / `np.argwhere(cond)` | indices where `cond` is True |
| `np.any(c)` / `np.all(c)` | at least one / all True |
| `(a > 0) & (b < 0)` | combine conditions (and); `~` is not; always use parentheses |
| `np.logical_or(c1, c2)` | combine conditions (or) |
| `np.isin(a, b)` | is each element of `a` in `b` |
| `np.isclose(a, b)` / `np.allclose(a, b)` | float comparison with tolerance (never use `==`) |
| `np.array_equal(a, b)` | same shape and same values |
| `np.count_nonzero(c)` | number of True values |

## Sorting, searching, counting

| Function | What it does |
|---|---|
| `np.sort(a)` | sorted copy |
| `np.argsort(a)` | indices that would sort `a` (use `-a` for descending) |
| `np.argpartition(a, k)` | indices of the `k` smallest values (fast, unordered) |
| `np.unique(a, return_counts=True)` | distinct values and their counts |
| `np.bincount(a)` | counts of each non-negative integer |
| `np.searchsorted(sorted_a, v)` | position where `v` would be inserted |
| `np.digitize(a, bins)` | bin index of each value |
| `np.histogram(a, bins)` | counts per bin and bin edges |

## Linear algebra

| Function | What it does |
|---|---|
| `A @ B` / `np.matmul(A, B)` | matrix product (`A * B` is element-wise!) |
| `np.dot(a, b)` | inner product of vectors |
| `np.outer(a, b)` | outer product |
| `np.einsum("ij,jk->ik", A, B)` | general sums of products via index notation |
| `np.trace(A)` | sum of the diagonal |
| `np.linalg.inv(A)` | matrix inverse |
| `np.linalg.solve(A, b)` | solve `Ax = b` (better than inverting) |
| `np.linalg.det(A)` | determinant |
| `np.linalg.norm(x, axis=)` | vector / matrix norm (L2 by default) |
| `np.linalg.eigh(S)` / `np.linalg.eig(A)` | eigenvalues and eigenvectors (symmetric / general) |
| `np.linalg.svd(A, full_matrices=False)` | singular value decomposition |
| `np.linalg.qr(A)` | QR decomposition |
| `np.linalg.cholesky(S)` | Cholesky factor of a positive definite matrix |
| `np.linalg.lstsq(X, y, rcond=None)` | least squares solution |
| `np.linalg.pinv(A)` | pseudo-inverse |
| `np.linalg.matrix_rank(A)` | rank |

## Broadcasting

Shapes are aligned from the **right**; two dimensions are compatible if they are equal or one of them is 1.

| Shapes | Result |
|---|---|
| `(n, d)` with `(d,)` | `(n, d)` |
| `(n, d)` with `(n, 1)` | `(n, d)` |
| `(n,)` with `(n, 1)` | `(n, n)` (classic bug) |

## Frequently used ML patterns

| Task | NumPy expression |
|---|---|
| Standardise features | `(X - X.mean(axis=0)) / X.std(axis=0)` |
| Min-max scaling | `(X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))` |
| Add intercept column | `np.c_[np.ones(n), X]` |
| One-hot encoding | `np.eye(K)[labels]` |
| Train/test indices | `idx = rng.permutation(n)` then split `idx` |
| Sigmoid | `1 / (1 + np.exp(-z))` |
| ReLU | `np.maximum(0, z)` |
| Softmax (stable) | `e = np.exp(z - z.max(axis=1, keepdims=True))` then `e / e.sum(axis=1, keepdims=True)` |
| MSE | `np.mean((y_hat - y) ** 2)` |
| Cross-entropy | `-np.mean(np.log(P[np.arange(n), labels]))` |
| Accuracy | `np.mean(pred == labels)` |
| Linear regression (OLS) | `np.linalg.lstsq(X, y, rcond=None)[0]` |
| Dense layer | `X @ W + b` |
| Cosine similarity | normalise rows with `/ np.linalg.norm(A, axis=1, keepdims=True)`, then `A @ B.T` |
| Log returns | `np.diff(np.log(prices))` |
| Rolling windows | `sliding_window_view(x, w)` from `numpy.lib.stride_tricks` |

## Saving, loading, interop

| Function | What it does |
|---|---|
| `np.save("f.npy", a)` / `np.load("f.npy")` | save / load one array (binary) |
| `np.savez("f.npz", X=X, y=y)` | save several arrays |
| `np.savetxt("f.csv", a, delimiter=",")` | save as text |
| `np.loadtxt("f.csv", delimiter=",")` | load from text |
| `pd.DataFrame(a)` / `df.to_numpy()` | NumPy ↔ pandas |
| `torch.from_numpy(a)` / `t.numpy()` | NumPy ↔ PyTorch (shares memory on CPU) |

## Slicing

### Position guide

`a[start:stop:step]` — start here, stop before there, jump this far. The indices sit **between** the elements:

```
          0   1   2   3   4   5   6   7   8   9     <- values
        |   |   |   |   |   |   |   |   |   |   |
        0   1   2   3   4   5   6   7   8   9  10   <- positions
```

`a[2:5]` takes everything between position 2 and position 5. It follows that:

- `len(a[i:j]) == j - i`
- `a[:k]` and `a[k:]` join back into `a`, with no gap and no overlap
- a negative `step` walks backwards, so `start` is then the larger index

### One axis

| Syntax | What it does |
|---|---|
| `a[:]` | everything; `start`, `stop` and `step` are all optional |
| `a[2:5]` | positions 2, 3, 4 |
| `a[:3]` / `a[7:]` | the first three / from 7 to the end |
| `a[-1]` / `a[-3:]` / `a[:-1]` | the last / the last three / all but the last |
| `a[::2]` | every second element |
| `a[m::k]` | every k-th element, starting at m |
| `a[::-1]` | reversed |
| `a[5:2:-1]` | backwards from position 5 down to 3 |

### Several axes

One slice per axis, in the same order as `.shape`.

| Syntax | What it does |
|---|---|
| `M[1, 2]` | a single element |
| `M[1]` / `M[1, :]` | row 1 |
| `M[:, 2]` | column 2 |
| `M[0:2, 1:3]` | a block |
| `M[:, ::-1]` | mirror left to right |
| `M[..., -1]` | the last entry of the last axis |
| `M[[0, 2]]` | rows 0 and 2 |
| `M[:, [0, 3]]` | columns 0 and 3 |
| `M[np.ix_(rows, cols)]` | the grid of the chosen rows and columns |
| `M[[0, 2], [1, 3]]` | the pairs (0,1) and (2,3), not a grid |
| `M[mask]` | the rows where the 1D `mask` is True |

### Integer or slice

| Syntax | Shape | Why |
|---|---|---|
| `M[1]` | `(4,)` | an integer removes the axis |
| `M[1:2]` | `(1, 4)` | a slice keeps it |
| `M[:, 2]` | `(3,)` | flat, neither a row nor a column |
| `M[:, 2:3]` | `(3, 1)` | a genuine column |
| `M[:, 2][:, None]` | `(3, 1)` | add the axis back |

### View or copy

| Syntax | What you get |
|---|---|
| `a[1:5]`, `a[:, 2]`, `a.T`, `a.reshape(...)` | a view: writing into it changes the original |
| `a[[0, 2]]`, `a[a > 0]` | a copy |
| `np.shares_memory(a, b)` | check which of the two you have |
| `a[1:5].copy()` | force an independent copy |

### Assigning into a slice

| Syntax | What it does |
|---|---|
| `X[:, 0] = 0` | overwrite a whole column |
| `X[X > 6] = 0` | overwrite everything above a threshold |
| `X[0:2, 1:3] = [[1, 2]]` | the right-hand side broadcasts into the slice |

### Boolean masks

| Syntax | What it does |
|---|---|
| `a[a > 0]` | the matching values, flattened to 1D |
| `M[M[:, 0] > 2]` | the rows where the condition holds |
| `np.flatnonzero(c)` | the positions where `c` is True |
| `c.sum()` / `c.mean()` | the number / the share of True values |
| `~c`, `c1 & c2`, `c1 \| c2` | not, and, or; each comparison in its own parentheses |

### Frequent slices

| Task | Slice |
|---|---|
| Line up t with t−1 | `x[1:]` against `x[:-1]` |
| First difference | `x[1:] - x[:-1]` |
| The last `w` observations | `x[-w:]` |
| Every k-th, starting at m | `x[m::k]` |
| Reverse the order | `x[::-1]` |
| The last column | `X[:, -1]` |
| Drop column j | `np.delete(X, j, axis=1)` |
| A chosen set of columns | `X[:, [0, 3]]` |
| The rows where a condition holds | `X[X[:, 0] > 0]` |
| The diagonal | `np.diag(S)` / `S[np.arange(n), np.arange(n)]` |
| Rolling windows | `sliding_window_view(x, w)` |
| Split at an index | `x[:k]` and `x[k:]` |

## Images

An image is a 3D array of shape `(height, width, channels)`. The channels are R, G, B, and sometimes a fourth alpha (transparency) channel. Values are either `uint8` from 0 to 255 or float from 0 to 1.

### Loading and displaying

| Function | What it does |
|---|---|
| `plt.imread(path)` | load a picture into an array |
| `img / 255` | rescale to [0, 1] when `img.dtype` is `uint8` |
| `img[:, :, :3]` | keep R, G, B and drop the alpha channel |
| `plt.imshow(img)` | display |
| `plt.axis("off")` | hide the axes |
| `plt.show()` | draw the figure |

### Inspecting

| Function | What it does |
|---|---|
| `img.ndim` | number of axes, 3 for a colour picture |
| `img.shape` | `(height, width, channels)` |
| `img.dtype` | `uint8` (0 to 255) or float (0 to 1) |
| `img.min()` / `img.max()` | the range of the values |

### Changing the picture

| Function               | What it does                                                  |
| ---------------------- | ------------------------------------------------------------- |
| `img.copy()`           | an independent copy, so the original stays unchanged          |
| `img2[:, :, 0] = 0`    | remove the red colour (0 = red, 1 = green, 2 = blue)          |
| `1 - img`              | invert, black becomes white (floats); `255 - img` for `uint8` |
| `np.flip(img, axis=1)` | mirror left to right (`axis=0` turns it upside down)          |
