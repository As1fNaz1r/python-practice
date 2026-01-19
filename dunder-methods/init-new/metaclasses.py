class Meta(type):
    def __new__(mcs, name, bases, dct):
        print(f"Metaclass creating class: {name}")
        return super().__new__(mcs, name, bases, dct)


class MyClass(metaclass=Meta):
    def __new__(cls):
        print("MyClass.__new__")
        return super().__new__(cls)
    
    def __init__(self):
        print("MyClass.__init__")


# Output when defining the class:
# Metaclass creating class: MyClass

obj = MyClass()
# MyClass.__new__
# MyClass.__init__
