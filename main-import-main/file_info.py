import os

print(f"__name__ = {__name__}")
print(f"__file__ = {__file__}")
print(f"Directory of this file: {os.path.dirname(__file__)}")
print(f"Filename only: {os.path.basename(__file__)}")

if __name__ == "__main__":
    print("This is the main program!")