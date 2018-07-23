'''
Future manages the execution and represents the eventual result of a computation

# method: 
done()
cancel()
result()
exception()
add_done_callback(fn)
await future # event loop pause execution until future is done
'''

loop.run_until_complete(future) # loop stops after future is complete

'''
# Task: a subclass of Future that is used to wrap and manage the execution of a coroutin in an event loop
'''


# Creating a task, wrap coroutine in a task
asyncio.ensure_future(coro_or_future, *, loop=None)

# or
AbstractEventLoop.create_task(coro)
