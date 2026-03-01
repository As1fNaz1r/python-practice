# The __name__ Variable
# Every module has a __name__ variable:

# If file is run directly: __name__ == "__main__"
# If file is imported: __name__ == "module_name"

# File: my_module.py
def hello():
    print("Hello from my_module!")

# This code only runs when file is executed directly
if __name__ == "__main__":
    print("Running my_module directly")
    hello()
Why this matters:

# File: main.py
import my_module  # Only imports, doesn't run the test code

my_module.hello()  # Calls the function
# Output: "Hello from my_module!"
# (The if __name__ == "__main__" block doesn't run)
# Running directly
$ python my_module.py
# Output: 
# Running my_module directly
# Hello from my_module!