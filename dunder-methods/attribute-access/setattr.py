class ValidatedPerson:
    def __setattr__(self, name, value):
        if name == "age" and value < 0:
            raise ValueError("age can not be negative")
        super().__setattr__(name,value)

p = ValidatedPerson()
p.age = 25
p.age = -5