# `__setattr__` - The Write Interceptor

## What It Does
Intercepts **EVERY** attribute assignment on an object.

## The Golden Rule
- Called whenever you do `obj.x = value`
- Runs for ALL assignments, including in `__init__`

## Basic Example
```python
class Logged:
    def __setattr__(self, name, value):
        print(f"Setting {name} = {value}")
        super().__setattr__(name, value)

obj = Logged()
obj.x = 10  # Prints: "Setting x = 10"
```

## Critical Rules

### 1. Always Use `super().__setattr__()` or `__dict__`
```python
# ❌ WRONG - Infinite recursion
def __setattr__(self, name, value):
    self.name = value  # Calls __setattr__ again!

# ✅ RIGHT - Option 1
def __setattr__(self, name, value):
    super().__setattr__(name, value)

# ✅ RIGHT - Option 2
def __setattr__(self, name, value):
    self.__dict__[name] = value
```

### 2. Called During `__init__`
```python
class Example:
    def __init__(self):
        self.x = 10  # Triggers __setattr__!
    
    def __setattr__(self, name, value):
        print(f"Setting {name}")
        super().__setattr__(name, value)

obj = Example()  # Prints: "Setting x"
```

## Use Cases

### 1. Validation
```python
class Person:
    def __setattr__(self, name, value):
        if name == "age":
            if not isinstance(value, int):
                raise TypeError("Age must be an integer")
            if value < 0:
                raise ValueError("Age cannot be negative")
        super().__setattr__(name, value)

p = Person()
p.age = 25      # OK
p.age = -5      # ValueError
p.age = "25"    # TypeError
```

### 2. Read-Only Attributes
```python
class Immutable:
    def __init__(self, value):
        super().__setattr__("value", value)
    
    def __setattr__(self, name, value):
        raise AttributeError("Cannot modify attributes")

obj = Immutable(10)
obj.value = 20  # AttributeError
```

### 3. Type Enforcement
```python
class Strict:
    _types = {"name": str, "age": int, "score": float}
    
    def __setattr__(self, name, value):
        if name in self._types:
            expected = self._types[name]
            if not isinstance(value, expected):
                raise TypeError(f"{name} must be {expected.__name__}")
        super().__setattr__(name, value)
```

### 4. Logging Changes
```python
class Audited:
    def __setattr__(self, name, value):
        if hasattr(self, name):
            old = getattr(self, name)
            print(f"Changed {name}: {old} → {value}")
        super().__setattr__(name, value)
```

### 5. Computed Attributes
```python
class Rectangle:
    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        if name in ("width", "height"):
            if hasattr(self, "width") and hasattr(self, "height"):
                super().__setattr__("area", self.width * self.height)

r = Rectangle()
r.width = 5
r.height = 10
print(r.area)  # 50
```

## Common Pitfalls

### 1. Infinite Recursion
```python
# ❌ BAD
def __setattr__(self, name, value):
    self.name = value  # Calls __setattr__ again!
```

### 2. Forgetting It Runs in `__init__`
```python
class Bad:
    def __init__(self):
        self.initialized = False
        self.value = 10  # __setattr__ runs, but initialized is False!
    
    def __setattr__(self, name, value):
        if not self.initialized:  # AttributeError!
            raise Exception("Not ready")
        super().__setattr__(name, value)
```

### 3. Breaking Inheritance
```python
# ❌ BAD - Doesn't call super()
def __setattr__(self, name, value):
    self.__dict__[name] = value  # Bypasses parent class logic
```

## When to Use
- Input validation
- Creating immutable objects
- Enforcing type constraints
- Logging/auditing changes
- Computed/dependent attributes
- ORM field assignment

## Performance Note
`__setattr__` adds overhead to every assignment. Use it when you need the control, but be aware of the cost in performance-critical code.
