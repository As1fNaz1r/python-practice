# Method 1: Import entire module

import calculator 
result1 = calculator.add(2,3)
result2 = calculator.mul(8,4)
result3 = calculator.divide(12,3)
print(result1)
print(result2)
print(result3)
# 5
# 32
# 4.0



# Method 2: Import specific functions
# File: main.py
from calculator import add, multiply

result = add(5, 3)      # 8 (no calculator. prefix)
result = multiply(4, 2)  # 8
# subtract() not available - wasn't imported


# Method 3: Import with alias

# # File: main.py
# import calculator as calc  # Shorter name



# Method 4: Import everything (not recommended)

# # File: main.py
# from calculator import *  # Imports ALL functions

