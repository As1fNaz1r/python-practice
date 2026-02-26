single = 'single quote'
double = "double quote"
triple = ''' tripe quotes
caan span
multiple line'''
print(single)
print(double)
print(triple)
# single quote
# double quote
#  tripe quotes
# caan span
# multiple line


text = "Hello, World!"

print(text[0])     # H (first character)
print(text[-1])    # ! (last character)
print(text[7:12])  # World (slice from index 7 to 11)
print(text[:5])    # Hello (first 5 characters)
print(text[7:])    # World! (from index 7 to end)
print(text[::2])   # Hlo ol! (every second character)


text = "Hello"
length = len(text)  # 5
