# __getattribute__ is the main door - EVERYONE must go through it, no exceptions


# __getattribute__ - The Main Door
# Every time you access ANY attribute on an object, Python calls this method first.


# obj.name        # Goes through __getattribute__
# obj.method()    # Goes through __getattribute__
# obj.__dict__    # Even this goes through __getattribute__!



# Every time you access ANY attribute on an object, Python calls this method first.
class Person:
    def __getattribute__(self,name):
        print(f"Someone is asking for: {name}")
        return super().__getattribute__(name)


p = Person()
p.age = 25
print(p.age)