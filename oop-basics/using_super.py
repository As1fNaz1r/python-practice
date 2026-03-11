# Sometimes you want to keep the parent's behavior AND add more. Use super().


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand,model)
        self.doors = doors
    
    def info(self):
        parent_info = super().info()
        return f"{parent_info} with {self.doors} doors"

car = Car("toyatta", "camry", 4)
print(car.info())

# output
# toyatta camry with 4 doors

# What super() does:
# Calls the parent class's method
# Lets you extend behavior instead of completely replacing it