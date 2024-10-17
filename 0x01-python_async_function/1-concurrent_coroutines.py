#!/usr/bin/env python3
"""importing packages"""

from typing import List
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random

"""a function that executes the program"""


async def wait_n(n: int, max_delay: int) -> list[float]:
    tasks = []
    for i in range(n):
        tasks.append(wait_random(max_delay))
    result = await asyncio.gather(*tasks)
    return (result)
