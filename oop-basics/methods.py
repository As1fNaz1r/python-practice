# Methods are just functions that belong to a class and can access the object's data via self.

class Reactangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 *(self.width+self.height)

    def scale(self, factor):
        self.width *= factor
        self.height *= factor


rect = Reactangle(5,3)
print(rect.area())
print(rect.perimeter())

rect.scale(2)
print(rect.area())

# output
# 15
# 16
# 60



# Methods can:

# Read object data (self.width)
# Modify object data (self.width *= factor)
# Take additional parameters (factor)
# Return values

