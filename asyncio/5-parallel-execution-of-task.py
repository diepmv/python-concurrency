'''
coroutine asyncio.wait(futures, *, loop=None, return_when=ALL_COMPLETE)

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
  completed, pending = await asyncio.wait(item_coros)

  print("results: {!r}".format(results))


loop = asyncio.get_event_loop()

try:
  loop.run_until_complete(get_items(4))
finally:
  loop.close()
