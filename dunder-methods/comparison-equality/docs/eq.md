# `__eq__` - Equality Comparison

## Overview
The `__eq__` method defines how objects of your class are compared for equality using the `==` operator.

## Syntax
```python
def __eq__(self, other):
    # Return True if equal, False if not equal
    # Return NotImplemented if comparison not supported
    pass
```

## Key Points

- Called when using `==` operator: `obj1 == obj2` calls `obj1.__eq__(obj2)`
- Should return `True`, `False`, or `NotImplemented`
- Return `NotImplemented` (not `False`) when comparison with other type isn't supported
- Python automatically generates `!=` from `__eq__` (you rarely need to define `__ne__`)

## Best Practices

1. **Type checking**: Always check if `other` is the right type
2. **Return NotImplemented**: For unsupported types, return `NotImplemented` not `False`
3. **Symmetric**: If `a == b`, then `b == a` should also be true
4. **Transitive**: If `a == b` and `b == c`, then `a == c`
5. **Consistent with `__hash__`**: If you define `__eq__`, objects that compare equal should have the same hash

## Common Pattern

```python
def __eq__(self, other):
    if not isinstance(other, MyClass):
        return NotImplemented
    return self.key_attribute == other.key_attribute
```

## Example Use Case

Comparing users by ID rather than by all attributes - two users with the same ID are considered equal even if other attributes differ.

## Related
- `__ne__` - Not equal comparison
- `__hash__` - Must be consistent with `__eq__`
- `is` operator - Identity comparison (different from equality)
