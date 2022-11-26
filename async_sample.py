import asyncio


async def async_function():
    await asyncio.sleep(2)
    print("Hello World!")


async def main():
    print("Start")
    for x in range(5):
        asyncio.ensure_future(async_function())

    print('Do some actions 1')
    await asyncio.sleep(2)
    print('Do some actions 2')
    await asyncio.sleep(2)
    print('Do some actions 3')

    await asyncio.gather(*asyncio.all_tasks() - {asyncio.current_task()})


asyncio.run(main())
