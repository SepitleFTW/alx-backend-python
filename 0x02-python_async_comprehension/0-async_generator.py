#!/usr/bin/env python3
"""
async gen
"""


import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module.
    """
    for noob in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
