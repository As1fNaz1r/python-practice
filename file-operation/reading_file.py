# read as string
with open("data.txt", "r") as file:
    content = file.read()
    print(content)


# read as list of lines
with open("data.txt", "r") as file:
    lines = file.readlines()
    for line in lies:
        print(f"Line: {line.strip()}")



# Read line by line (memory efficient for large files)
with open("data.txt", "r"):
    for line in file:
        print(line.strip())


# Reading specific amounts

with open("data.txt", "r") as file:
    first_100 = file.read(100)  # Read first 100 characters
    next_line = file.readline()  # Read next line
    remaining = file.read()      # Read everything left