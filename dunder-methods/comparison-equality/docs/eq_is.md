# `==` vs `is` - Equality vs Identity

## Overview
Understanding the difference between `==` (equality) and `is` (identity) is crucial in Python.

## Key Differences

| Operator | Checks | Method Called | Use Case |
|----------|--------|---------------|----------|
| `==` | Value equality | `__eq__` | Are the contents the same? |
| `is` | Identity (same object) | None | Are they the same object in memory? |

## Examples

```python
a = [1, 2]
b = [1, 2]
c = a

a == b  # True - same contents
a is b  # False - different objects in memory
a is c  # True - same object (c points to a)
```

## When to Use Each

### Use `==` (Equality)
- Comparing values/contents
- Most common use case
- Checking if two objects are equivalent

```python
user1 = User(id=1, name="Alice")
user2 = User(id=1, name="Alice")
user1 == user2  # True if __eq__ compares by value
```

### Use `is` (Identity)
- Checking for `None`: `if x is None:`
- Checking for singletons: `True`, `False`, `None`
- Performance: `is` is faster (just compares memory addresses)
- Checking if two variables reference the same object

```python
if result is None:  # ✅ Correct
    pass

if result == None:  # ❌ Less idiomatic
    pass
```

## Important Notes

1. **`is` cannot be overridden** - it always checks object identity
2. **`==` can be customized** - by defining `__eq__`
3. **Small integers and strings are cached** - may behave unexpectedly

```python
a = 256
b = 256
a is b  # True - Python caches small integers

a = 257
b = 257
a is b  # False (usually) - not cached

a = "hello"
b = "hello"
a is b  # True - string interning
```

## Best Practices

1. Use `is` only for `None`, `True`, `False`, or when you specifically need identity
2. Use `==` for all other comparisons
3. Never use `is` to compare numbers, strings, or custom objects (unless checking identity is your goal)

## Common Patterns

```python
# ✅ Correct
if value is None:
    pass

if flag is True:  # Usually just: if flag:
    pass

# ❌ Wrong
if name is "Alice":  # Use ==
    pass

if count is 0:  # Use ==
    pass
```

## Related
- `__eq__` - Defines equality behavior
- `id()` - Returns object's memory address
- Object identity and memory management
