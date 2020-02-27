---
title: "Iterables, Iterators, and Generators"
draft: true
---


# Iterables

**Iterables are objects that hold elements, from which element can be pulled one at a time**. Most containers are iterables. In python, some well known examples are:

- **list**, deque, ...
- **set**, frozensets, ...
- **dict**, defaultdict, OrderedDict, Counter, ...
- **tuple**, namedtuple, ...
- **str**

Many other things like open files, open sockets, etc are also iterables, but they are not containers.

`Summary: iterables are containers, or container-like objects from which an element can be pulled one at a time`.

# Iterators

**Iterators are stateful iterables**. They are simply iterables plus an `__next__()` method implementation. An **iterator** can be obtained by passing an **iterable** to `iter()`.

```
>>> a = [1, 2, 3] # list is an iterable
>>> b = iter(a) # pass iterable a to iter() to create iterator b
>>> type(b)

list_iterator
```


You can pass an **iterator** to `next()` to get an element. But you can not pass an **iterable** to `next()`. This is because **iterables are stateless,** `next()` does not know which element to return.

```
>>> next(a) # pass an iterable to next() will give you an error

Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'list' object is not an iterator

>>> next(b) # pass iterator b to next() to get an element from b
1
```

*The **itertools** module implements a list of functions for creating many kinds of iterators.*

```
>>> # example
>>> from itertools import *
>>> numbers = cycle(range(10)) # create an iterator with infinite numbers cycling through 0 ~ 0
>>> for _ in range(15):
>>> 	print(next(numbers))

0
1
2
3
4
5
6
7
8
9
0
1
2
3
4

 ```


# Generators

A generator is a special kind of iterators. It allows you to write iterators in an elegant syntax that avoids writing classes with `__iter__()` and `__next__()` methods. 

Implementing a generator is very simple. You just need to add a `yield` statement inside your function.

```
>>> def foo():
>>>     yield
>>> 
>>> print(type(foo()))

<class 'generator'>
```

The above code creates a generator but it is not useful at all.

## When will you need a generator?

**Whenever you need to grab one element at a time from a container-like thing, you can use a generator, no mater weather there is finite or infinite elements in your container**.

We can create a **CounterDown** class using Generator.

```
>>> def counter(number=5):
>>>     end = False
>>>     while not end:
>>>         yield number
>>>         number -= 1
>>>         if number <= 0:
>>>             end = True
>>>     print("End")
>>> 
>>> c = counter(5)
>>> for i in c:
>>>     print(i)

5
4
3
2
1
end
```

You just write you **loop logic** regularly, then you insert a `yield` statement for the variable that you want to return at each loop step. Implementing a generator is that simple!

## Types of Generators

There are two types of generators in Python: generator **functions** and generator **expressions**. A generator function is any function in which the keyword `yield` appears in its body. We just saw an example of that. The appearance of the keyword `yield` is enough to make the function a generator function.

The other type of generators are the generator equivalent of a list comprehension. Its syntax is really elegant for a limited use case.

```
>>> g = (i for i in range(100))
>>> print(type(g))

<class 'generator'>
```    

**Generator expressions allow us to quickly create generators**.