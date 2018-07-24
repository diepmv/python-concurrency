'''
coroutine asyncio.wait(futures, *, loop=None, timeout=None,return_when=ALL_COMPLETE)

itself it is coroutine, take a list of tasks, notify event loop when all complete, return value is two set of value

return (DONE_FUTURES, PENDDING_FUTURES)
'''

import asyncio

async def get_item(i):
  await asyncio.sleep(i)
  return 'item ' str(i)


async def get_items(num_items):
  print("getting items")
  item_coros = [get_item(i) for i in range(num_items)]

  print("wating for tasks to complete")
  completed, pending = await asyncio.wait(item_coros, timeout=2)

  print("results: {!r}".format(results))

  if pending:
    print("canceling remaining tasks")
    for t in pending:
      t.cancel()


loop = asyncio.get_event_loop()

try:
  loop.run_until_complete(get_items(4))
finally:
  loop.close()


'''
coroutine asyncio.wait_for(future, timeout, *, loop=None)
When have only coroutine or task
'''


try:
  result = await.asyncio.wait_for(task, 30.0)
except asyncio.TimeoutError:
  print('task did not complete in 30 seconds so it was canceled')


'''
asyncio.as_complete(fs, *, loop=None, timeout=None)
Yield the tasks as they complete
'''

for task in asyncio.as_complete(tasks):
  result = await task

'''
asyncio.gather(*coros_or_futures, loop=None, return_exceptions=False)
Instead of returning collection of futures, return single future that aggregrates the result from the past and future, aggregrated in order of the original sequence
'''
async def get_item(i):
  await asyncio.sleep(i)
  return 'item ' str(i)


async def get_items(num_items):
  print("getting items")
  item_coros = [get_item(i) for i in range(num_items)]

  print("wating for tasks to complete")
  completed, pending = await asyncio.gather(item_coros, timeout=2)

  print("results: {!r}".format(results))

  if pending:
    print("canceling remaining tasks")
    for t in pending:
      t.cancel()


loop = asyncio.get_event_loop()

try:
  loop.run_until_complete(get_items(4))
finally:
  loop.close()

