# __float__ is called when you use float(obj) on your object.

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __float__(self):
        return self.numerator/self.denominator

    def __int__(self):
        return int(self.numerator/self.denominator)

half = Fraction(5,10)
third = Fraction(1,3)

print(half)
print(float(half))
print(float(third))
print(int(half))

# output
# <__main__.Fraction object at 0x103e93fd0>
# 0.5
# 0.3333333333333333
# 0