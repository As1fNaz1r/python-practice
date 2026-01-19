"""A simple calculator module"""

def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

# This runs only when the file is executed directly
if __name__ == "__main__":
    print("Calculator Program")
    print("-" * 20)
    
    # Get user input
    try:
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, *, /): ")
        num2 = float(input("Enter second number: "))
        
        # Perform calculation
        if operation == "+":
            result = add(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            result = "Invalid operation"
        
        print(f"Result: {result}")
        
    except ValueError:
        print("Please enter valid numbers!")