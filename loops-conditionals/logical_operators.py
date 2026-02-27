age = 25
has_licence = True
has_car = False

# AD both must be true
if age > 18 and has_licence:
    print("you can legally drive")

# OR at least one must be true
if age > 18 or has_licence:
    print("you can legally drive or have a car")

# NOT reverses the condition
if not has_car:
    print("you have a car")
