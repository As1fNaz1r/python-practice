# Threading (Multiple Workers)
# Imagine hiring 2 workers. Each does one task.

import threading 
import time

def make_coffee():
    print("Grinding beans")
    time.sleep(3)
    print("coffee ready")

def make_toast():
    print("Toasting bread")
    time.sleep(2)
    print("Toast ready")


# start both at once

thread1 = threading.Thread(target=make_coffee)
thread2 = threading.Thread(target=make_toast)

thread1.start()
thread2.start()

# wait for both to finish
thread1.join()
thread2.join()

# output
# Grinding beans
# Toasting bread
# Toast ready
# coffee ready

# When to use: IO-bound tasks (waiting for files, network, user input)