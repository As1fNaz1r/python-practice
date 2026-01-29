# Async (One Smart Worker)
# One worker who switches between tasks when waiting.
# When to use: IO-bound tasks with lots of waiting (web requests, database queries)

import asyncio
async def make_coffee():
    print("Grinding beans")
    await asyncio.sleep(3)
    print("Coffee ready")

async def make_toast():
    print("Toastinng bread")
    await asyncio.sleep(2)
    print("toast ready")

async def main():
    await asyncio.gather(make_coffee(), make_toast())

asyncio.run(main())

# output
# Grinding beans
# Toastinng bread
# toast ready
# Coffee ready


# CPU-bound vs IO-bound
# IO-bound (Use Async or Threading)
# Waiting for external things:

# Reading files
# Network requests
# Database queries
# User input
# async def fetch_url(url):
#     # Waiting for network response
#     await http_client.get(url)
# Why async works: While waiting for response, do other tasks.

# CPU-bound (Use Multiprocessing)
# Heavy computation:

# Math calculations
# Image processing
# Video encoding
# Data analysis