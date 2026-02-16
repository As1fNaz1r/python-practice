class Person:
    def __new__(cls, name, age):
        instance = super().__new__(cls)
        print(instance)
        return instance

    def __init__(self, name, age):
        print("init run")
        self.name = name
        self.age = age
        print(name, age)
    

person = Person("Asif","23")

# output 
# <__main__.Person object at 0x10bc73f10>
# init run
# Asif 23
