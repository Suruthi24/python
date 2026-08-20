import asyncio

async def task(name):
    print(name, "started")
    await asyncio.sleep(2)
    print(name, "finished")

async def main():
    await asyncio.gather(
        task("Task 1"),
        task("Task 2"),
        task("Task 3")
    )
asyncio.run(main())