# Part 5: Package Structure (Multiple Modules)
# A package is a directory containing Python modules.


Basic package structure
my_package/
├── __init__.py     # Makes this a package (can be empty)
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
Importing from packages
# Import from package
import my_package.module1
from my_package import module2
from my_package.subpackage import module3

# Import specific items
from my_package.module1 import some_function
from my_package.subpackage.module3 import SomeClass
The __init__.py file
This file makes a directory a Python package. It can be empty or contain initialization code.


# File: my_package/__init__.py
# This runs when package is imported

print("my_package is being imported!")

# You can expose items at package level
from .module1 import important_function
from .module2 import useful_class

# Now users can do:
# from my_package import important_function
# Instead of:
# from my_package.module1 import important_function