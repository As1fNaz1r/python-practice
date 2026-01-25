# __exit__ - Cleanup Phase
# __exit__ is called when leaving the with block. It receives three parameters about any exception that occurred.

# Parameters:
# exc_type: Type of exception (or None)
# exc_value: Exception instance (or None)
# exc_traceback: Traceback object (or None)


class SimpleFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        print(f'opening {self.filename}')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # This ALWAYS runs, even if there's an error
        print(f'closing {self.filename}')
        if self.file:
            self.file.close()

        # Return False to propagate exceptions
        # Return True to suppress them
        return False

with SimpleFile("test.txt") as f:
    f.write("hello world")


# output
# file creation with hello world in it