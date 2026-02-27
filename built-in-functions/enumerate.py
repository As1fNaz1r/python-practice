fruits = ["apple", "banana", "cherrry"]

#without enumerate
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# with ennumerate
for i, fruit in enumerate(fruits):
    print(f"{i}:{fruit}")
# 0: apple
# 1: banana
# 2: cherrry
# 0:apple
# 1:banana
# 2:cherrry

for i, fruit in enumerate(fruits, start=10):
    print(f"{i}:{fruit}")
# 10:apple
# 11:banana
# 12:cherrry