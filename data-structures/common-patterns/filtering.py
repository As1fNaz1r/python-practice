# keep onl positive numbers
numbers = [5, -2, 0, 8, -1, 3]
positive = [n for n in numbers if n>0]
print(positive)
# [5, 8, 3]


# Using filter() functions
positive = list(filter(lambda x: x>0, numbers))
print(positive)
# [5, 8, 3]