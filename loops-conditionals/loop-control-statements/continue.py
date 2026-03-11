# continue - Skip current iteration


numbers = [5,-2,4,5,2,-5,-6,3]
for num in numbers:
    if num <0:
        continue
    print(f"positive numbers: {num}")