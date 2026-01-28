

def greet(name):
    return f"Hello, {name}"

def add(a, b):
    return a+b

def is_even(num):
    return num%2 == 0


operations = [greet, add, is_even]
# call them by index
print(operations[0]("asif"))
print(operations[1](12,11))
print(operations[2](5))

# output
# Hello, asif
# 23
# False