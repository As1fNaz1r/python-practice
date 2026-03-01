def add(a,b):
    return a+b 

if __name__ == "__main__":
    # How do you know it works?
    print(add(2, 3))  # 5 - looks good!
    # But what about:
    # add(2.5, 3.5)  # 6.0?
    # add(-1, 1)     # 0?
    # add("2", "3")  # Should this work?


# Perfect! Now it only prints "all test passed" and not the 5.

# The if __name__ == "__main__": block ensures that the code inside it only runs when the file is executed directly (like python3 without_test.py), not when it's imported as a module.

# So when you run python3 with_tests.py:

# Python imports without_test
# The add function is defined
# The if __name__ == "__main__": block is skipped (because __name__ is "without_test", not "__main__")
# Your test runs and prints "all test passed"