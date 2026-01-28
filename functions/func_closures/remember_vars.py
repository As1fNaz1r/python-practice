#  Functions can create other functions that "remember" variables from their parent scope.

# def add(a, b):
#     return 5  # returns a number

# def make_adder():
#     def add(a, b):
#         return a + b
#     return add  # returns a function!


def make_multiplier(n):
    def multiply(x):
        return x*n 
    return multiply

times_2 = make_multiplier(2)
times_3 = make_multiplier(3)

print(times_2(5))
print(times_3(5))

# outer() runs and gives you back inner
# my_func now holds that inner function
# my_func() calls it


# The magic: Even though make_multiplier finished running, the multiply function still remembers what 
# type_checking.py was!
# times_2 remembers n=2
# times_3 remembers n=3