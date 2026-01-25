# __call__ - Making Objects Callable Like Functions
# __call__ lets you use an object as if it were a function. When you do obj(), Python calls obj.__call__().

# Why is this useful?
# Create objects that remember state between calls
# Make classes that act like functions but with memory


class Counter:
    def __init__(self):
        self.count = 0
    def __call__(self):
        self.count += 1
        return self.count

counter = Counter()
print(counter())
print(counter())
print(counter())
print(counter())

# output
# 1
# 2
# 3
# 4

# __call__:
# Makes objects callable like functions: obj()
# Useful for objects that need to remember state
# Syntax: def __call__(self, *args, **kwargs):




# What it does
# obj(...)
# Calls:
# obj.__call__(...)