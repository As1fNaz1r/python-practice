unique_squares = {x*x for x in range(-5,6)}
print(unique_squares)
# {0, 1, 4, 9, 16, 25}

words = ["apple", "banana", "apricot", "bears"]
first_letter = {word[0] for word in words}
print(first_letter)
# {'a', 'b'}