class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"

p = Person("Alice", 30)
print(str(p))
print(repr(p))
print(p)

# Output
# Alice, 30 years old
# Person(name='Alice', age=30)
# Alice, 30 years old


# str(obj)      # calls __str__
# repr(obj)     # calls __repr__
# print(obj)    # calls __str__ (falls back to __repr__ if __str__ not defined)
# f"{obj}"      # calls __str__
# f"{obj!r}"    # calls __repr__


# The Golden Rule for __repr__
# Ideally, repr(obj) should return a string that, when passed to eval(), recreates the object:

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __repr__(self):
#         return f"Point({self.x}, {self.y})"

# p = Point(3, 4)
# print(repr(p))  # Point(3, 4)

# # This should work:
# p2 = eval(repr(p))  # Creates new Point(3, 4)
# When to Define What
# Only __repr__: When one representation is enough (Python will use it for both)

# class Coordinate:
#     def __init__(self, lat, lon):
#         self.lat = lat
#         self.lon = lon
    
#     def __repr__(self):
#         return f"Coordinate({self.lat}, {self.lon})"
# Both: When you need different representations for users vs developers

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
    
#     def __str__(self):
#         return f"Account for {self.owner}: ${self.balance:.2f}"
    
#     def __repr__(self):
#         return f"BankAccount(owner={self.owner!r}, balance={self.balance})"

# acc = BankAccount("Bob", 1500.50)
# print(str(acc))   # Account for Bob: $1500.50
# print(repr(acc))  # BankAccount(owner='Bob', balance=1500.5)
# Practical Examples
# Container classes:

# class ShoppingCart:
#     def __init__(self):
#         self.items = []
    
#     def add(self, item):
#         self.items.append(item)
    
#     def __str__(self):
#         if not self.items:
#             return "Empty cart"
#         return f"Cart with {len(self.items)} items"
    
#     def __repr__(self):
#         return f"ShoppingCart(items={self.items!r})"
# Date/Time-like objects:

# class Duration:
#     def __init__(self, hours, minutes):
#         self.hours = hours
#         self.minutes = minutes
    
#     def __str__(self):
#         return f"{self.hours}h {self.minutes}m"
    
#     def __repr__(self):
#         return f"Duration(hours={self.hours}, minutes={self.minutes})"

# d = Duration(2, 30)
# print(f"Meeting length: {d}")      # Meeting length: 2h 30m
# print(f"Debug info: {d!r}")        # Debug info: Duration(hours=2, minutes=30)
# Common Patterns
# Using !r in format strings to get repr of nested objects:

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
    
#     def __repr__(self):
#         # Use !r to get repr of strings (with quotes)
#         return f"Book(title={self.title!r}, author={self.author!r})"

# b = Book("1984", "Orwell")
# print(repr(b))  # Book(title='1984', author='Orwell')
# Collections showing their contents:

# class Team:
#     def __init__(self, name, members):
#         self.name = name
#         self.members = members
    
#     def __str__(self):
#         member_list = ", ".join(self.members)
#         return f"Team {self.name}: {member_list}"
    
#     def __repr__(self):
#         return f"Team(name={self.name!r}, members={self.members!r})"
# Interactive Shell Behavior
# In the Python REPL:

# >>> p = Person("Alice", 30)
# >>> p
# Person(name='Alice', age=30)  # Shows __repr__

# >>> print(p)
# Alice, 30 years old  # Shows __str__
# Quick Tips
# Always define __repr__ - it's more important than __str__
# Make __repr__ unambiguous - include class name and key attributes
# Make __str__ readable - think about what users want to see
# Use !r in f-strings when building __repr__ to properly quote strings
# If you only define one, define __repr__ - Python will use it for both