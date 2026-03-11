# Part 6: Relative vs Absolute Imports
# Absolute imports (recommended)
# File: my_package/subpackage/module.py
# Import from parent or sibling packages
from my_package import module1          # From parent
from my_package.subpackage import module2  # From sibling
Relative imports (within same package)
# File: my_package/subpackage/module.py
# . means current directory
# .. means parent directory

from . import sibling_module      # Import from same directory
from .. import parent_module      # Import from parent directory
from .sibling import some_function  # Import from sibling module
Example:

math_utils/
├── __init__.py
├── basic.py        # add, subtract
├── advanced.py     # sqrt, power
└── geometry/
    ├── __init__.py
    ├── circle.py   # area_circle
    └── rectangle.py # area_rectangle

# File: math_utils/geometry/circle.py
from ..basic import multiply  # Relative import
from math import pi           # Standard library import

def area_circle(radius):
    return multiply(pi, radius * radius)





# Quick Reference
# Import syntax:

# import module - Import entire module
# from module import item - Import specific item
# import module as alias - Import with alias
# from module import * - Import all (avoid)
# Key concepts:

# Module = Python file (.py)
# Package = Directory with __init__.py
# __name__ = "__main__" if run directly, else module name
# __init__.py = Makes directory a package
# Best practices:

# Group imports (stdlib, third-party, local)
# Use absolute imports (from package import module)
# Avoid circular imports
# Use if __name__ == "__main__" for executable code
# Be explicit (don't use import *)
# Common patterns:

# Config module for settings
# Utils module for helper functions
# Models module for data classes
# Main module with main() function