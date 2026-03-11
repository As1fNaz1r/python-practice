words = ["apple", "banana", "apricot", "blueberry"]
grouped = {}
for word in words:
    first_letter = word[0]
    if first_letter not in grouped:
        grouped[first_letter] = []
    grouped[first_letter].append(word)

print(grouped)
# {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}