
# self is just a reference to the current object. Think of it as "me" or "this object".

class Dog:
    def __init__(self, name):
        self.name = name  # "My name is..."
    
    def bark(self):
        print(f"{self.name} says Woof!")  # "I say Woof!"

dog1 = Dog("Buddy")
dog2 = Dog("Max")

dog1.bark()  # Buddy says Woof!
dog2.bark()  # Max says Woof!

# When you call dog1.bark():

# Python automatically passes dog1 as the first argument
# So it's really calling Dog.bark(dog1)
# Inside the method, self refers to dog1


# Why we need self:

class Counter:
    def __init__(self):
        self.count = 0  # Each counter has its own count
    
    def increment(self):
        self.count += 1  # Modify THIS counter's count

c1 = Counter()
c2 = Counter()

c1.increment()
c1.increment()
c2.increment()

print(c1.count)  # 2
print(c2.count)  # 1
# Each object has its own data. self lets you access that specific object's data.