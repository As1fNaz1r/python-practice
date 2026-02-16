# `__getattribute__` - The Gatekeeper

## What It Does
Intercepts **EVERY** attribute access on an object. No exceptions.

## The Golden Rule
- Called for ALL attribute access: `obj.x`, `obj.method()`, `obj.__dict__`
- Always runs first, before any other lookup

## Basic Example
```python
class Logger:
    def __getattribute__(self, name):
        print(f"Accessing: {name}")
        return super().__getattribute__(name)

obj = Logger()
obj.value = 10
print(obj.value)  # Prints "Accessing: value" then 10
```

## Critical Rules

### 1. Always Use `super()`
```python
# ❌ WRONG - Infinite recursion
def __getattribute__(self, name):
    return self.__dict__[name]  # Calls __getattribute__ again!

# ✅ RIGHT
def __getattribute__(self, name):
    return super().__getattribute__(name)
```

### 2. Even Special Attributes Go Through It
```python
obj.__dict__    # Goes through __getattribute__
obj.__class__   # Goes through __getattribute__
obj.__str__     # Goes through __getattribute__
```

## Use Cases
- **Proxies**: Forward all attribute access to another object
- **Security**: Check permissions before allowing access
- **Debugging**: Log every attribute access
- **ORMs**: Database field access (Django, SQLAlchemy)
- **Lazy loading**: Load heavy objects only when accessed

## When to Use
Only when you need to intercept **every single** attribute access. For most cases, use `__getattr__` instead (safer, no recursion risk).

## Common Pitfalls
1. Forgetting `super()` → infinite recursion
2. Accessing `self.anything` inside the method → infinite recursion
3. Using it when `__getattr__` would suffice → unnecessary complexity
