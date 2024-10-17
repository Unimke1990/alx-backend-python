#!/usr/bin/env python3
"""module that defines the measure_time function"""
import random
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for `wait_n(n, max_delay)`"""
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()

    total_time = start_time - end_time
    return total_time / n
