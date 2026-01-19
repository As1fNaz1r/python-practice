# Metaclasses in Python

## Overview
Metaclasses are "classes that create classes". They control how classes themselves are created, not how instances are created.

## Key Concepts

### What is a Metaclass?
- A metaclass is a class that inherits from `type`
- `type` is Python's built-in metaclass
- When you define a class, Python uses a metaclass to create it
- By default, all classes use `type` as their metaclass

### Metaclass `__new__` Parameters
- `mcs` - the metaclass itself
- `name` - name of the class being created (string)
- `bases` - tuple of base classes
- `dct` - dictionary of class attributes and methods

## Execution Timeline

```
1. Class Definition Time:
   Meta.__new__() is called → Creates the MyClass class object

2. Instance Creation Time:
   MyClass.__new__() is called → Creates instance
   MyClass.__init__() is called → Initializes instance
```

## Code Example

```python
class Meta(type):
    def __new__(mcs, name, bases, dct):
        print(f"Metaclass creating class: {name}")
        return super().__new__(mcs, name, bases, dct)

class MyClass(metaclass=Meta):
    def __new__(cls):
        print("MyClass.__new__")
        return super().__new__(cls)
    
    def __init__(self):
        print("MyClass.__init__")

# Output when defining the class:
# Metaclass creating class: MyClass

obj = MyClass()
# MyClass.__new__
# MyClass.__init__
```

## Common Use Cases

1. **Class Registration**: Automatically register classes in a registry
2. **Validation**: Enforce rules about class structure
3. **Auto-generation**: Add methods or attributes automatically
4. **ORM Frameworks**: Django models use metaclasses
5. **Singletons**: Enforce singleton pattern at class level
6. **API Design**: Create domain-specific languages (DSLs)

## Important Notes

- Metaclasses run at **class definition time**, not at import time
- They're powerful but complex - use sparingly
- Most problems can be solved with class decorators or `__init_subclass__`
- "Metaclasses are deeper magic than 99% of users should ever worry about" - Tim Peters
