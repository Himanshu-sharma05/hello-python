# sometimes we have to use libraries that are blocking (like standard database drivers or heavy file operations).
# this code solves those problems
import asyncio
from concurrent.futures import ThreadPoolExecutor
import time 

def blockingCode(name):
    print(f"Fetching the details of the user:{name}")
    time.sleep(3)
    print(f"Hello {name}")

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool,blockingCode,"Himanshu")
        print(result)

asyncio.run(main())