squares = {x:x*x for x in range(10)}
print(squares)

# output
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {values:keys for keys, values in original.items()}
print(swapped)

# output
# {1: 'a', 2: 'b', 3: 'c'}

# Filter dictionnary
scores = {"Alice": 85, "bob":72, "Charlie": 90, "David": 65}
good_scores = {name:score for name, score in scores.items() if score>=80}
print(good_scores)

# output
# {'Alice': 85, 'Charlie': 90}