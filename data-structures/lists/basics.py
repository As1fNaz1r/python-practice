fruits = ["apple", "banana", "orange"]
numbers =[1,2,3,4,5]
mixed = ["hello", 42, 3.14, True]


# accessinng elements
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])
print(fruits[-1:-3])


# Modifying lists
fruits.append("grape")      # Add to end
fruits.insert(1, "mango")   # Insert at position 1
fruits.remove("banana")     # Remove by value
popped = fruits.pop()       # Remove and return last item
fruits[0] = "kiwi"          # Change first item

