---
title: "(tabular data) Conditionally Remove Groups in pandas.DataFrame.groupby"
draft: true
---

# Create DataFrame

```python
import pandas as pd

g = list('aaaabbbccdddd')
df = pd.DataFrame({
    'g': g,
    'v': range(len(g)),
})
df
```

``` 
    g   v
0   a   0
1   a   1
2   a   2
3   a   3
4   b   4
5   b   5
6   b   6
7   c   7
8   c   8
9   d   9
10  d  10
11  d  11
12  d  12
```

# Remove groups that have less than 4 rows

## Define an `apply` function

The function checks the number of rows of each sub-DataFrame in a group. If the DataFrame has 4 or more rows, return
the DataFrame as is. Otherwise, it returns an empty DataFrame.

```python
def remove_small_groups(df):
    if len(df) < 4:
        return pd.DataFrame()
    else:
        return df
```

## Apply the function

```python
df.groupby('g') \
    .apply(remove_small_groups) \
    .reset_index(drop=True) # drop index created by `groupby()`
```

```
   g     v
0  a   0.0
1  a   1.0
2  a   2.0
3  a   3.0
4  d   9.0
5  d  10.0
6  d  11.0
7  d  12.0 
```


