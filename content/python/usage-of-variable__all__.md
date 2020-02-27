# Usage of Variable `__all__`
---

`__all__` specifies all the objects in the module that will be imported to the namespace. For example, the module.py file has the following code in it.

```
__all__ = ['x', 'foo']

x = 1
y = 2
def foo(): return 3

```

If we use from module import *, object x and foo will be available in the namespace, but y is not. But we can use from module import y to explicitly add y to the namespace.