from threading import Thread
from queue import Queue

def producer(queue):
  for i in range(10):
    item = make_an_item_available(i)
    queue.put(item)


def consumer(queue):
  while True:
    item = queue.get()
    # do something with item
    queue.task_done() # mask the item as done

queue = Queue()
t1 = Thread(target=producer, args=(queue,))
t2 = Thread(target=consumer, args=(queue,))

t1.start()
t2.start()
