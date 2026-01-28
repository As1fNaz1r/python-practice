

def pass_functions(func, value):
    return func(value)

def uppercase(text):
    return text.upper()

def lowercase(text):
    return text.lower()

def reverse(text):
    return text[::-1]

print(pass_functions(uppercase, "asif"))
print(pass_functions(lowercase, "aSIf"))
print(pass_functions(reverse, "asif"))

# output
# ASIF
# asif
# fisa