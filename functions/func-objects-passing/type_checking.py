def greet(name):
    return f"Hello, {name}"

def add(a, b):
    return a+b

def is_even(num):
    return num%2 == 0

print("what type are functios")
print(type(greet), type(add), type(is_even))


say_hello = greet
caalculator = add
checker = is_even

print(say_hello)
print(caalculator)
print(checker)


# calling them through new names
print(say_hello("asif"))
print(caalculator(5,3))
print(checker(4))

# prove they are the same object

print(f"remember they are same, {greet is say_hello}")
print(caalculator is add)
print( is_even is checker)

# output
# what type are functios
# <class 'function'> <class 'function'> <class 'function'>
# <function greet at 0x1005ceb80>
# <function add at 0x1005cec10>
# <function is_even at 0x1005ceca0>
# Hello, asif
# 8
# True
# remember they are same, True
# True
# True
