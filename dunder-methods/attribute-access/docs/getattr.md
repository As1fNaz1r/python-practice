# `__getattr__` - The Fallback

## What It Does
Called **ONLY** when an attribute is NOT found through normal lookup.

## The Golden Rule
- Only runs if attribute doesn't exist
- Much safer than `__getattribute__` (no recursion risk)
- Your "Plan B" for missing attributes

## Basic Example
```python
class Flexible:
    def __init__(self):
        self.name = "Alice"
    
    def __getattr__(self, name):
        return f"'{name}' not found, here's a default"

obj = Flexible()
print(obj.name)    # "Alice" (found normally)
print(obj.age)     # "'age' not found, here's a default"
```

## Attribute Lookup Order
When you access `obj.x`, Python searches:
1. Instance `__dict__` (obj's own attributes)
2. Class `__dict__` (class attributes)
3. Parent classes (inheritance chain)
4. **Call `__getattr__`** ← Only if not found above
5. Raise `AttributeError` if `__getattr__` doesn't exist

## Use Cases

### 1. Default Values
```python
class Config:
    def __getattr__(self, name):
        return None  # Return None for any missing config
```

### 2. Dynamic Attributes
```python
class APIClient:
    def __getattr__(self, endpoint):
        return f"https://api.example.com/{endpoint}"

api = APIClient()
print(api.users)     # "https://api.example.com/users"
print(api.products)  # "https://api.example.com/products"
```

### 3. Backward Compatibility
```python
class OldAPI:
    def __init__(self):
        self.new_name = "value"
    
    def __getattr__(self, name):
        if name == "old_name":
            return self.new_name  # Redirect old attribute
        raise AttributeError(f"No attribute {name}")
```

### 4. Lazy Loading
```python
class User:
    def __getattr__(self, name):
        if name == "profile":
            print("Loading profile from database...")
            self._profile = {"age": 30, "city": "NYC"}
            return self._profile
        raise AttributeError
```

## Important Notes

### Won't Be Called If Attribute Exists (Even If None)
```python
class Test:
    def __init__(self):
        self.x = None  # x EXISTS
    
    def __getattr__(self, name):
        return "default"

t = Test()
print(t.x)  # None (not "default")
print(t.y)  # "default" (y doesn't exist)
```

### No Recursion Risk
```python
class Safe:
    def __getattr__(self, name):
        return self.other_attr  # Safe! Won't cause recursion
```

## When to Use
- Providing default values for missing attributes
- Creating dynamic/computed attributes
- Building API wrappers or proxies
- Maintaining backward compatibility

**Prefer `__getattr__` over `__getattribute__` unless you specifically need to intercept ALL access.**
