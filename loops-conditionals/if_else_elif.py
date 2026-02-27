age = 20
if age>= 18:
    print("you can vote")
    print("Welcome")


temperature = 25

if temperature > 30:
    print("its hot outside")
else:
    print("its not too hot")


score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'

print(f"your grade: {grade}")

# Equality
x == y    # x equals y
x != y    # x not equal to y

# Numeric comparisons
x > y     # x greater than y
x < y     # x less than y
x >= y    # x greater than or equal to y
x <= y    # x less than or equal to y

# Identity (same object)
x is y    # x and y are the same object
x is not y  # x and y are different objects

# Membership
x in y    # x is in collection y
x not in y  # x is not in collection y
