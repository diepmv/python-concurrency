'''
Coroutine:
+Cotoutine function: special function can give up control to its caller without losing its state
+Coroutine object

'''

# 1

import asyncio

# coroutine function
async def say_hello():
  print("hello world")

loop = asyncio.get_event_loop()
loop.run_util_complete(say_hello())
loop.close()


# 2

async def delayed_hello():
  print("hello")
  await asyncio.sleep(1) # tell python to pause execution and return control to event loop until event occurs
  print("world")

loop = asyncio.get_event_loop()
loop.run_until_complete(delayed_hello())
loop.close()

# coroutineObject = coroutineFunction()
'''
to execute coroutine object,need to wrap it in a Future object
and pass it to running event loop
'''
