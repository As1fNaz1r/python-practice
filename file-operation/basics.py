#old way
file = open("data.txt", "r")
content = file.read()
file.close() # What if error happens before this?


with open("data1.txt", "r") as file:
    content = file.read()
# File automatically closes here, even if error occurs


# Why with is better:

# Automatically closes the file
# Handles errors gracefully
# Cleaner code