with open("output.txt", "w") as file:
    file.write("hey Asif writing \n")
    file.write("second line \n")
    file.write("third line \n")


# writing multiple lines at once
lines = ["Line 1 \n", "Line 2 \n", "Line 3 \n"]

with open("output.txt", "w") as file:
    file.writelines(lines)




# File Modes Cheat Sheet
# Mode	Description	File exists?	File doesn't exist?
# "r"	Read only	Opens file	Error
# "w"	Write	Overwrites	Creates new
# "a"	Append	Adds to end	Creates new
# "r+"	Read & write	Opens file	Error
# "w+"	Read & write	Overwrites	Creates new
# "a+"	Read & append	Adds to end	Creates new
# "rb"	Read binary	Opens file	Error
# "wb"	Write binary	Overwrites	Creates new
# Most common:

# "r" - Reading text files
# "w" - Writing text files
# "a" - Appending to logs
# "rb" - Reading images, PDFs, etc.