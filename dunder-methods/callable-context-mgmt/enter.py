# Context Managers - __enter__ and __exit__
# Context managers are used with the with statement. They help you set up and clean up resources automatically.

# The Pattern:
# with something as variable:
#     # Do stuff
# # Cleanup happens automatically
# How it works:
# __enter__ runs when entering the with block
# Your code runs
# __exit__ runs when leaving the block (even if there's an error!)



# __enter__ - Setup Phase
# __enter__ is called when you enter the with block. Whatever it returns becomes the variable after as.



class SimpleFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        # This runs when entering 'with' block
        print(f"Opening {self.filename}")
        self.file = open(self.filename, 'w')
        return self.file  # This becomes the 'as' variable

# Using it:
with SimpleFile("test.txt") as f:
    f.write("Hello!")
# File is handled automatically

