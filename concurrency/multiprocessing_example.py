# Multiprocessing (Multiple Kitchens)
# Imagine having 2 separate kitchens. Each has its own everything.

import multiprocessing
import time

def heavy_calculations(n):
    total = 0
    for i in range(n):
        total += i*i
    return total

# run on 2 CPU cores
if __name__ == "__main__":
    with multiprocessing.Pool(2) as pool:
        result = pool.map(heavy_calculations, [10000000, 10000000])
        print(result)


# On macOS (and Windows), multiprocessing uses spawn, not fork.
# That means:
# Every child process re-imports your Python file from scratch
# So when Python hits this line:
# with multiprocessing.Pool(2) as pool:
# it executes it again inside the child, which tries to create more processes, which try to import again…
# 🔁 infinite process spawning loop
# Python detects this and stops you with:
# RuntimeError: An attempt has been made to start a new process
# before the current process has finished its bootstrapping phase