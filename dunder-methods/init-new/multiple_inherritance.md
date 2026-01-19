# Multiple Inheritance and `__new__`

## Overview
This example demonstrates how `__new__` behaves with multiple inheritance and the Method Resolution Order (MRO).

## Key Concepts

### Method Resolution Order (MRO)
- Python uses C3 linearization algorithm to determine method lookup order
- `super()` follows the MRO, not just the immediate parent
- For `class C(A, B)`, the MRO is: `C → A → B → object`

### `super()` in Multiple Inheritance
- `super().__new__(cls)` calls the next class in the MRO
- Each class's `__new__` should call `super().__new__(cls)` to continue the chain
- This ensures all parent `__new__` methods are called

## Execution Flow

```
1. C.__new__() is called
2. super() in C calls A.__new__() (next in MRO)
3. super() in A calls B.__new__() (next in MRO)
4. super() in B calls object.__new__() (creates the instance)
5. Instance is returned back through the chain
```

## Code Example

```python
class A:
    def __new__(cls):
        print("A.__new__")
        return super().__new__(cls)

class B:
    def __new__(cls):
        print("B.__new__")
        return super().__new__(cls)

class C(A, B):
    def __new__(cls):
        print("C.__new__")
        return super().__new__(cls)

c = C()
```

## Output
```
C.__new__
A.__new__
B.__new__
```

## MRO Visualization

```
C(A, B)
  ↓
  A
  ↓
  B
  ↓
object
```

You can check the MRO with: `print(C.__mro__)`

## Best Practices

1. Always use `super()` instead of calling parent classes directly
2. Always pass `cls` to `super().__new__(cls)`
3. Ensure all classes in the hierarchy cooperate with `super()`
4. Be aware of the MRO when debugging multiple inheritance issues
