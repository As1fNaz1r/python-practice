print(f"The value of __name__ is: {__name__}")

def greet(name):
    return f"Hello, {name}!"

# This code only runs when the file is executed directly
if __name__ == "__main__":
    print("This file is being run directly!")
    print(greet("World"))
    print("Doing some main program stuff...")