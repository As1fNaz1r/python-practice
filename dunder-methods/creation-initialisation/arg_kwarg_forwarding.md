# Argument Forwarding Between `__new__` and `__init__`

## Overview
This example demonstrates how arguments are automatically forwarded from `__new__` to `__init__` in Python.

## Key Concepts

### Automatic Argument Forwarding
- When you call `Person("Alice", age=30)`, Python passes these arguments to both `__new__` and `__init__`
- `__new__` receives: `cls, "Alice", age=30`
- `__init__` receives: `self, "Alice", age=30`
- The instance returned by `__new__` becomes `self` in `__init__`

### Using `*args` and `**kwargs`
- `*args`: Captures positional arguments as a tuple
- `**kwargs`: Captures keyword arguments as a dictionary
- Useful when `__new__` doesn't need to process arguments, just forward them

## Code Example

```python
class Person:
    def __new__(cls, *args, **kwargs):
        print(f'__new__ receive: {args}, {kwargs}')
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name, age):
        print(f'__init received: {name}, {age}')
        self.name = name
        self.age = age

p = Person("Alice", age=30)
p = Person("bob", age=33)
```

## Output
```
__new__ receive: ('Alice',), {'age': 30}
__init received: Alice, 30
__new__ receive: ('bob',), {'age': 33}
__init received: bob, 33
```

## Argument Flow Diagram

```
Person("Alice", age=30)
        ↓
__new__(cls, *args, **kwargs)
  args = ("Alice",)
  kwargs = {"age": 30}
        ↓
  returns instance
        ↓
__init__(self, name, age)
  self = instance from __new__
  name = "Alice"
  age = 30
```

## Common Patterns

### Pattern 1: `__new__` with `*args, **kwargs`
When `__new__` doesn't need to inspect arguments:
```python
def __new__(cls, *args, **kwargs):
    return super().__new__(cls)
```

### Pattern 2: `__new__` with Specific Parameters
When `__new__` needs to process arguments:
```python
def __new__(cls, name, age):
    print(f"Creating person: {name}")
    return super().__new__(cls)
```

### Pattern 3: Different Signatures
`__new__` and `__init__` can have different signatures:
```python
def __new__(cls, *args, **kwargs):
    # Process or validate before instance creation
    if not args:
        raise ValueError("Name required")
    return super().__new__(cls)

def __init__(self, name, age=0):
    self.name = name
    self.age = age
```

## Use Cases

1. **Validation**: Check arguments before creating instance
2. **Logging**: Track instance creation with arguments
3. **Caching**: Return cached instance based on arguments
4. **Factory Pattern**: Create different types based on arguments

## Important Notes

- Arguments must be compatible between `__new__` and `__init__`
- If `__new__` doesn't return an instance of `cls`, `__init__` won't be called
- `__new__` is a static method (receives `cls`, not `self`)
- `__init__` is an instance method (receives `self`)
