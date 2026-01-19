"""Common patterns with __name__ == "__main__" """

def main():
    """Main function - good practice to put main logic here"""
    print("Running the main program...")
    print("This makes code more organized and testable!")

def some_utility_function():
    """A utility function that can be imported"""
    return "I'm a utility function!"

# Pattern 1: Simple if __name__ == "__main__"
if __name__ == "__main__":
    main()

# Pattern 2: You might also see this style
# if __name__ == "__main__":
#     # Direct code here instead of calling main()
#     print("Direct code execution")

# Pattern 3: Sometimes with argument parsing
# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) > 1:
#         print(f"Command line argument: {sys.argv[1]}")
#     main()