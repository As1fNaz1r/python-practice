# __new__ with *args and **kwargs Forwarding

class Person:
    def __new__(cls, *args, **kwargs):
        print(f'__new__ receive: {args}, {kwargs}')
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name, age):
        print(f'__init received: {name}, {age}')
        self.name = name
        self.age = age


p = Person("Alice", age=30)

p = Person("bob", age=33)