# `NotImplemented` - Comparison Fallback

## Overview
`NotImplemented` is a special singleton value that tells Python "I don't know how to compare with this type, try the other object's method."

## Key Difference: `NotImplemented` vs `False`

### Returning `False`
```python
def __eq__(self, other):
    if not isinstance(other, MyClass):
        return False  # ❌ Wrong - blocks other class from trying
    return self.value == other.value
```

### Returning `NotImplemented`
```python
def __eq__(self, other):
    if not isinstance(other, MyClass):
        return NotImplemented  # ✅ Correct - allows fallback
    return self.value == other.value
```

## How Python Handles Comparisons

When you write `a == b`, Python tries:

1. `a.__eq__(b)` - If returns `NotImplemented`, continue
2. `b.__eq__(a)` - If returns `NotImplemented`, continue
3. Fall back to identity comparison `a is b`

## Why This Matters

```python
class A:
    def __eq__(self, other):
        if not isinstance(other, A):
            return NotImplemented  # Give B a chance
        return True

class B:
    def __eq__(self, other):
        return True  # B knows how to compare with anything

a = A()
b = B()

# a == b
# Step 1: a.__eq__(b) → NotImplemented (b is not an A)
# Step 2: b.__eq__(a) → True (B accepts anything)
# Result: True
```

If `A.__eq__` returned `False` instead, Python would never try `B.__eq__`, and the result would be `False`.

## Best Practice

**Always return `NotImplemented` for unsupported types**, not `False` or `True`.

```python
def __eq__(self, other):
    if not isinstance(other, self.__class__):
        return NotImplemented
    # Your comparison logic here
```

## Benefits

1. **Symmetric comparisons**: Both classes get a chance to handle the comparison
2. **Extensibility**: Other classes can define how to compare with your class
3. **Proper type handling**: Respects Python's comparison protocol

## Common Mistake

```python
# ❌ Wrong
def __eq__(self, other):
    if type(other) != MyClass:
        return False  # Blocks other class from trying

# ✅ Correct
def __eq__(self, other):
    if not isinstance(other, MyClass):
        return NotImplemented  # Allows fallback mechanism
```

## Related
- `__eq__` - Equality comparison
- `__ne__` - Not equal comparison
- Comparison protocol in Python
