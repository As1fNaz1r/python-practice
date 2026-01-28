def say_hello():
    print("hello")

def wrapper():
    print("Before")
    say_hello()
    print("After")



say_hello1 = wrapper
say_hello1()