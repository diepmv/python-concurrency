import threading

cond = threading.Condition()

# Consumer one item
cond.acquire()
while not an_item_is_available():
  cond.wait()
get_an_available_item()
cond.release()


# Producer one item
cond.acquire()
make_an_item_available()
cond.notify()
cond.release()


