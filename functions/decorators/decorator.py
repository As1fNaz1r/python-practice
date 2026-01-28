def say_hello():
    print("hello")
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper


@my_decorator
def say_hello():
    print("hello")

say_hello()
# output
# Before
# hello
# After

# Outer function takes something (number or function)
# Inner function remembers it
# Return the inner function
# Inner function still has access to what it remembered