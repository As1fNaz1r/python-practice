# `__ne__` - Not Equal Comparison

## Overview
The `__ne__` method defines how objects are compared for inequality using the `!=` operator.

## Syntax
```python
def __ne__(self, other):
    return not self.__eq__(other)
```

## Key Points

- Called when using `!=` operator: `obj1 != obj2` calls `obj1.__ne__(obj2)`
- **You rarely need to define this** - Python automatically generates it from `__eq__`
- By default: `__ne__` returns `not __eq__`

## When to Define It

Only define `__ne__` if inequality has special logic different from `not ==`:

- Custom inequality semantics
- Performance optimization (rare)
- Legacy Python 2 compatibility (not needed in Python 3)

## Default Behavior (Python 3+)

```python
# Python automatically does this:
def __ne__(self, other):
    result = self.__eq__(other)
    if result is NotImplemented:
        return NotImplemented
    return not result
```

## Best Practice

**Don't define `__ne__` unless you have a specific reason.** Just define `__eq__` and let Python handle `!=`.

## Example of When You Might Define It

```python
class SpecialCase:
    def __eq__(self, other):
        # Complex expensive comparison
        return expensive_equality_check(self, other)
    
    def __ne__(self, other):
        # Fast inequality check without full comparison
        return quick_inequality_check(self, other)
```

## Related
- `__eq__` - Equality comparison
- `NotImplemented` - Fallback mechanism
