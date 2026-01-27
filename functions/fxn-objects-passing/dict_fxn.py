
# Functions are objects of type <class 'function'>
# You can assign them to variables
# They maintain their identity (is returns True)
# You can call them through new names

def greet(name):
    return f"Hello, {name}"

def add(a, b):
    return a+b

def is_even(num):
    return num%2 == 0
# map names to functions
tools = {
    'greeter': greet,
    'calculator': add,
    'checker': is_even
}

# call them by key
print(tools['greeter']('from dictionary way'))
print(tools['calculator'](3,2))
print(tools['checker'](4))

# output
# Hello, from dictionary way
# 5
# True

# Think of it like:
# greet is like holding a tool
# greet("Asif") is like using that tool
