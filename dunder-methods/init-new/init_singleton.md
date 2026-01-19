# Singleton Pattern with `__new__` and `__init__`

## Overview
This example shows how to implement the Singleton pattern and prevent `__init__` from running multiple times.

## The Problem

When implementing a singleton with `__new__`, `__init__` is still called every time you create an "instance", even though the same instance is returned.

```python
# Without the _initialized flag:
s1 = Singleton()  # __init__ runs
s2 = Singleton()  # __init__ runs again on the SAME instance!
```

## The Solution

Use a flag to track whether initialization has already occurred.

## Key Concepts

### Singleton Pattern
- Ensures only one instance of a class exists
- All references point to the same object
- Useful for configuration objects, database connections, logging, etc.

### Implementation Details
- `_instance`: Class variable storing the single instance
- `_initialized`: Class variable tracking initialization state
- `__new__`: Returns existing instance or creates new one
- `__init__`: Only runs initialization logic once

## Code Example

```python
class Singleton:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not Singleton._initialized:
            print("initialized once")
            self.data = []
            Singleton._initialized = True

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # True - same object
```

## Output
```
initialized once
```

## Execution Flow

```
First call: Singleton()
1. __new__ creates instance, stores in _instance
2. __init__ runs, sets _initialized = True

Second call: Singleton()
1. __new__ returns existing _instance
2. __init__ runs but skips initialization (already initialized)
```

## Alternative Approaches

### Using a Decorator
```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class MyClass:
    pass
```

### Using a Metaclass
```python
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
```

## When to Use

- Configuration managers
- Database connection pools
- Logger instances
- Cache managers
- Thread pools

## Cautions

- Can make testing difficult (shared state)
- Can hide dependencies
- Not thread-safe without additional locking
- Consider dependency injection as an alternative
