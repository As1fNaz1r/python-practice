Part 6: Relative vs Absolute Imports
Absolute imports (recommended)
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