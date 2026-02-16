# `__repr__` and `__str__` in Python

## The Key Difference

- **`__str__`**: For end users - readable, informal representation
- **`__repr__`**: For developers - unambiguous, ideally recreatable representation

Think of it this way:
- `__str__` is what you show to your users
- `__repr__` is what you show to yourself when debugging

## When They're Called

```python
str(obj)      # calls __str__
repr(obj)     # calls __repr__
print(obj)    # calls __str__ (falls back to __repr__ if __str__ not defined)
f"{obj}"      # calls __str__
f"{obj!r}"    # calls __repr__
```

## Basic Example

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        # User-friendly
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        # Developer-friendly, shows how to recreate
        return f"Person(name={self.name!r}, age={self.age!r})"

p = Person("Alice", 30)
print(str(p))   # Alice, 30 years old
print(repr(p))  # Person(name='Alice', age=30)
print(p)        # Alice, 30 years old (uses __str__)
```

## The Golden Rule for `__repr__`

Ideally, `repr(obj)` should return a string that, when passed to `eval()`, recreates the object:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
print(repr(p))  # Point(3, 4)

# This should work:
p2 = eval(repr(p))  # Creates new Point(3, 4)
```

## When to Define What

### Only `__repr__`: When one representation is enough

Python will use it for both if `__str__` is not defined.

```python
class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    
    def __repr__(self):
        return f"Coordinate({self.lat}, {self.lon})"
```

### Both: When you need different representations

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"Account for {self.owner}: ${self.balance:.2f}"
    
    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self.balance})"

acc = BankAccount("Bob", 1500.50)
print(str(acc))   # Account for Bob: $1500.50
print(repr(acc))  # BankAccount(owner='Bob', balance=1500.5)
```

## Practical Examples

### Container Classes

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)
    
    def __str__(self):
        if not self.items:
            return "Empty cart"
        return f"Cart with {len(self.items)} items"
    
    def __repr__(self):
        return f"ShoppingCart(items={self.items!r})"
```

### Date/Time-like Objects

```python
class Duration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def __str__(self):
        return f"{self.hours}h {self.minutes}m"
    
    def __repr__(self):
        return f"Duration(hours={self.hours}, minutes={self.minutes})"

d = Duration(2, 30)
print(f"Meeting length: {d}")      # Meeting length: 2h 30m
print(f"Debug info: {d!r}")        # Debug info: Duration(hours=2, minutes=30)
```

## Common Patterns

### Using `!r` in Format Strings

Use `!r` to get repr of nested objects (adds quotes to strings):

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __repr__(self):
        # Use !r to get repr of strings (with quotes)
        return f"Book(title={self.title!r}, author={self.author!r})"

b = Book("1984", "Orwell")
print(repr(b))  # Book(title='1984', author='Orwell')
```

### Collections Showing Their Contents

```python
class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members
    
    def __str__(self):
        member_list = ", ".join(self.members)
        return f"Team {self.name}: {member_list}"
    
    def __repr__(self):
        return f"Team(name={self.name!r}, members={self.members!r})"
```

## Interactive Shell Behavior

In the Python REPL:

```python
>>> p = Person("Alice", 30)
>>> p
Person(name='Alice', age=30)  # Shows __repr__

>>> print(p)
Alice, 30 years old  # Shows __str__
```

## Quick Tips

1. **Always define `__repr__`** - it's more important than `__str__`
2. **Make `__repr__` unambiguous** - include class name and key attributes
3. **Make `__str__` readable** - think about what users want to see
4. **Use `!r` in f-strings** when building `__repr__` to properly quote strings
5. **If you only define one**, define `__repr__` - Python will use it for both

## Summary Table

| Method | Purpose | Audience | Example Output |
|--------|---------|----------|----------------|
| `__str__` | Human-readable | End users | "Alice, 30 years old" |
| `__repr__` | Unambiguous, recreatable | Developers | "Person(name='Alice', age=30)" |
