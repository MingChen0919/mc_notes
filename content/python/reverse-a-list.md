---
title: "Reverse a list"
draft: true
---

# list[m:n:k]

* `m` is start. By default, m = 0.
* `n` is end. By default, n = len(list).
* `k` is step.


`l[m:n:k]` is basically `[l[m+k], l[m+2*k], l[m+3*k]], l[m+j*k]]` until `m+j*k > n`.


```
>>> x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x[2:8:2]

[2, 4, 6]
```

To verse a list, we can do:

```
>>> x[::-1]

[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
``` 