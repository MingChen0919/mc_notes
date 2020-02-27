---
title: "(datetime data) Convert TimeSeries Series or DataFrame to Specified Frequency"
draft: true
---

# Create a TimeSeries Series and TimeSeries DataFrame

A `TimeSeries` Series or DataFrame is a pandas object which has a `DatatimeIndex` index, and the datetime values
in the index should be sorted in time.

```python
index = [pd.to_datetime('2020-02-18') + pd.DateOffset(hours=np.random.randint(1, 25),
                                                      minutes=np.random.randint(1, 60))
         for _ in range(10)]
df = pd.DataFrame({
    'x': range(len(index))
}, index=index)

df

```

```
                     x
2020-02-18 10:14:00  0
2020-02-18 06:18:00  1
2020-02-18 17:16:00  2
2020-02-18 23:47:00  3
2020-02-18 04:13:00  4
2020-02-19 00:32:00  5
2020-02-18 03:27:00  6
2020-02-18 19:57:00  7
2020-02-18 22:14:00  8
2020-02-18 16:33:00  9
```

# Convert data to hourly data

## 'Truncate' datetime index to hour

```python
df['index'] = df.index.floor('H')
df = df.set_index('index')
df
```

```
                     x
index                 
2020-02-18 10:00:00  0
2020-02-18 06:00:00  1
2020-02-18 17:00:00  2
2020-02-18 23:00:00  3
2020-02-18 04:00:00  4
2020-02-19 00:00:00  5
2020-02-18 03:00:00  6
2020-02-18 19:00:00  7
2020-02-18 22:00:00  8
2020-02-18 16:00:00  9
```

## Sort datetime in index by time

```python
df = df.sort_index()
df
```

```
                     x
index                 
2020-02-18 03:00:00  6
2020-02-18 04:00:00  4
2020-02-18 06:00:00  1
2020-02-18 10:00:00  0
2020-02-18 16:00:00  9
2020-02-18 17:00:00  2
2020-02-18 19:00:00  7
2020-02-18 22:00:00  8
2020-02-18 23:00:00  3
2020-02-19 00:00:00  5
```

## Convert `df` to hourly data

Missing hours will be filled with NaN.

```python
df.asfreq('H')
```

```
                       x
index                   
2020-02-18 03:00:00  6.0
2020-02-18 04:00:00  4.0
2020-02-18 05:00:00  NaN
2020-02-18 06:00:00  1.0
2020-02-18 07:00:00  NaN
2020-02-18 08:00:00  NaN
2020-02-18 09:00:00  NaN
2020-02-18 10:00:00  0.0
2020-02-18 11:00:00  NaN
2020-02-18 12:00:00  NaN
2020-02-18 13:00:00  NaN
2020-02-18 14:00:00  NaN
2020-02-18 15:00:00  NaN
2020-02-18 16:00:00  9.0
2020-02-18 17:00:00  2.0
2020-02-18 18:00:00  NaN
2020-02-18 19:00:00  7.0
2020-02-18 20:00:00  NaN
2020-02-18 21:00:00  NaN
2020-02-18 22:00:00  8.0
2020-02-18 23:00:00  3.0
2020-02-19 00:00:00  5.0
```