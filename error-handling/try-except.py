try:
    result = 10/0
except ZeroDivisionError:
    print("Can't divide by zero")

try:
    number = int(input("Enter the nnumber"))
    result = 10/number

except ValueError:
    print("thats not a valid number")

except ZeroDivisionError:
    print("cant divide by zero")
