try:
    file = open("data.txt", "r")
    data = file.read()

except FileNotFoundError:
    print("File not found")
finally:
    file.close()

# output
# file.close()
# NameError: name 'file' is not defined