# Child Classes Inherit Different Property Values From Same Parent Class
---

# Create Parent and Child Classes

Child Class `Son` and `Daughter` use `super()` to access the attribute `__init__()` from their common parent 
class `Dad`. The initialized attributes will be inherited by its child Classes.

```python
class Dad:
    def __init__(self, available_money):
        self.inherited_money = 'Inherited ${} from Data'.format(available_money)

class Son(Dad):
    def __init__(self):
        super(Son, self).__init__(available_money = 10000)

class Daughter(Dad):
    def __init__(self):
        super(Daughter, self).__init__(available_money=50000)
```

# Create Instances for `Son` and `Daughter`

```python
son = Son()
print('Son: {}'.format(son.inherited_money))

daughter = Daughter()
print('Daughter: {}'.format(daughter.inherited_money))
```

``` 
Son: Inherited $10000 from Data
Daughter: Inherited $50000 from Data
```

The two classes have the same parent class and are initialized the same way, but resulting instances have different
property values.