# The Else Clause Runs only if NO exception occurred:

try:
    file = open("data.txt", "r")

except FileNotFoundError:
    print("File not found")
else:
    print("file opened successfully")
    content = file.read()
    file.close()
