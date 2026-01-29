import time
def make_coffee():
    print("Grinding beans")
    time.sleep(3)
    print("Coffee ready")

def make_toast():
    print("Toasting bread...")
    time.sleep(2)
    print("Toast ready")

make_coffee()
make_toast()

# output
# Grinding beans
# Coffee ready
# Toasting bread...
# Toast ready

# Problem: You wait for coffee before starting toast. Wasteful!

# Real Life
# You start coffee, then while it's brewing, you make toast. Both happen "at the same time."
# That's concurrency - doing multiple things in overlapping time periods.