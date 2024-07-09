#!/usr/bin/env python3
"""
task 1- Import async_generator from the previous task and then
write a coroutine
called async_comprehension that takes no arguments
"""


import typing

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> typing.List[float]:
    """
    make 10 numbers
    """

    return [rand async for rand in async_generator()]
