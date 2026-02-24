# Creating sets
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}
empty_set = set()  # Not {} (that's a dict!)

# Sets automatically remove duplicates
colors = {"red", "blue", "red", "green"}
print(colors)  # {"red", "blue", "green"}

# Common operations
fruits.add("grape")         # Add element
fruits.remove("banana")     # Remove element (error if missing)
fruits.discard("banana")    # Remove if exists (no error)
popped = fruits.pop()       # Remove and return random element
fruits.clear()              # Empty the set

# Set operations (like math sets)
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # Union: {1, 2, 3, 4, 5, 6}
print(A & B)   # Intersection: {3, 4}
print(A - B)   # Difference: {1, 2}
print(A ^ B)   # Symmetric difference: {1, 2, 5, 6}

# Membership tests (very fast!)
print(3 in A)  # True
print(7 in A)  # False


# Set methods cheat sheet:

# add(x) - Add element
# remove(x) - Remove element (error if missing)
# discard(x) - Remove if exists
# union(other) - All elements from both
# intersection(other) - Common elements
# difference(other) - Elements in first not in second
# issubset(other) - Check if all elements in other
# issuperset(other) - Check if contains all of other