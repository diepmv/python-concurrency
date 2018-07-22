'''
Coroutine:
Cotoutine function: special function can give up control to its caller without losing its state
and Coroutine object

'''

# 2

import asyncio

async def say_hello():
  print("hello world")

loop = asyncio.get_event_loop()
loop.run_util_complete(say_hello())
loop.close()


# 2

async def delayed_hello():
  print("hello")
  await asyncio.sleep(1)
  print("world")

loop = asyncio.get_event_loop()
loop.run_until_complete(delayed_hello())
loop.close()

# coroutineObject = coroutineFunction()
