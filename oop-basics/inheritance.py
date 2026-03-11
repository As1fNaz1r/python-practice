# Inheritance lets you create a new class based on an existing class. 
# The new class gets all the features of the parent, plus you can add more.



class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says woof!")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow")


dog = Dog("Buddy")
cat = Cat("whiskers")

dog.eat()
cat.sleep()

dog.bark()
cat.meow()

# output
# Buddy is eating
# whiskers is sleeping
# Buddy says woof!
# whiskers says Meow

# The relationship:

# Dog is an Animal (has all Animal features)
# Cat is an Animal (has all Animal features)
# But Dog is not a Cat