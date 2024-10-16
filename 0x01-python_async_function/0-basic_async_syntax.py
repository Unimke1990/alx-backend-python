import asyncio

async def myfucnt():
        print("starting my function")
        await asyncio.sleep(3)
        print("continuing my work after waiting")

        asyncio.run(myfucnt())