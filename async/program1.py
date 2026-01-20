import asyncio

async def getAndGreetUsers(name):
    print(f"Fetching details for user :{name}")
    await asyncio.sleep(3)
    print(f"Hello {name} details fetched successfully")

async def main():
    await asyncio.gather(
        getAndGreetUsers("Himanshu"),
        getAndGreetUsers("Dexter"),
        getAndGreetUsers("Hisenberg")
    )

asyncio.run(main())