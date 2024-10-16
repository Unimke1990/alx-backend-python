#!/urs/bin/env python3
"""
importing need packages
"""
import asyncio
import random


"""function that returns time delayed"""
async def wait_random(max_delay: int = 10) -> float:
    waitTime = random.uniform(0, max_delay)
    await asyncio.sleep(waitTime)
    print(waitTime)
    return waitTime   
asyncio.run(wait_random())   
    