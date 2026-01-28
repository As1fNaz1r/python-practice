

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

value1 = counter()
value2 = counter()
print(value1())
print(value1())
print(value2())

# output
# 1
# 2
# 1

# The nonlocal Rule
# Reading is free:

# def outer():
#     x = 10
#     def inner():
#         print(x)  # Just reading? No problem!
#     return inner
# Writing needs permission:

# def outer():
#     x = 10
#     def inner():
#         x = x + 1  # ERROR! Can't modify without nonlocal
#     return inner
# Fix with nonlocal:


# def outer():
#     x = 10
#     def inner():
#         nonlocal x  # "Let me modify the outer x"
#         x = x + 1
#         return x
#     return inner