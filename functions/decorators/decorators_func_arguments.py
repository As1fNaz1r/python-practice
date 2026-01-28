
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print(result)
        print("After")        
    return wrapper

@my_decorator
def add(a,b):
    return a+b

add(3,5)

# output
# Before
# 8
# After