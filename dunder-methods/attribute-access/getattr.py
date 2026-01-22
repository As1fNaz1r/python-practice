
# This only runs when Python can't find the attribute normally. It's your "Plan B".

class Robot:
    def __init__(self):
        self.name = "R2D2"
    def __getattr__(self, name):
        return f"I doon't have '{name}', but here's a default message"


r = Robot()
print(r.name)
print(r.weapon)



# How Python Looks for Attributes (The Search Order)
# When you do obj.x, Python searches in this order:

# Instance dictionary (obj.__dict__) - "Does this specific object have it?"
# Class dictionary - "Does the class definition have it?"
# Parent classes - "Do any parent classes have it?"
# Call __getattr__ - "Okay, let's use the fallback"
# Raise AttributeError - "Give up, it doesn't exist"