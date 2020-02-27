# Difference between @staticmethod and @classmethod
---


* `@staticmethod`: When you want to use a method from a class but you don't want to create an instance of that class, you use `@staticmethod` to decorate the method.

* `@classmethod` When you want to use a method from a class and you want to pass some data from the class to the method, and you still don't want to create an instance of that class, you use `@classmethod` to decorate the method.
module.py


```
class Fruit(object):
    FRUITS = ['orange', 'banana', 'apple', 'grape']

    @classmethod
    def add_fruit(cls, fruit: str):
        cls.FRUITS.append(fruit)
        return cls.FRUITS

    @staticmethod
    def upper_case_fruit(fruit: str):
        return fruit.upper()


print(Fruit.add_fruit('peach'))
print(Fruit.upper_case_fruit('peach'))
```

`cls` in the @classmethod decorated function is like `self`, which allows `add_fruit()` to access properties and methods of class Fruit.