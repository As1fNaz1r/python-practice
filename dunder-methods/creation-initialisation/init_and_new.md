# `__init__` and `__new__` Basics

## Overview
This example demonstrates the fundamental relationship between `__new__` and `__init__` in Python object creation.

## Key Concepts

### `__new__` Method
- Called **first** when creating an object
- Responsible for creating and returning the instance
- Must return an instance (usually by calling `super().__new__(cls)`)
- Receives the class as the first parameter (`cls`)

### `__init__` Method
- Called **after** `__new__` returns an instance
- Responsible for initializing the instance with attributes
- Does not return anything (implicitly returns `None`)
- Receives the instance as the first parameter (`self`)

## Execution Order

```
1. Person.__new__(cls, "Asif", "23")  → Creates instance
2. Person.__init__(self, "Asif", "23") → Initializes instance
```

## Code Example

```python
class Person:
    def __new__(cls, name, age):
        instance = super().__new__(cls)
        print(instance)  # Shows the created instance
        return instance

    def __init__(self, name, age):
        print("init run")
        self.name = name
        self.age = age
        print(name, age)

person = Person("Asif", "23")
```

## Output
```
<__main__.Person object at 0x...>
init run
Asif 23
```

## When to Use

- **`__new__`**: When you need to control instance creation (singletons, immutable types, subclassing immutable types like `int` or `str`)
- **`__init__`**: For normal instance initialization (most common use case)
