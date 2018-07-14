import threading

lock = threading.Lock()
lock.acquire()
try:
  # access shared resource
finally:
  lock.release()


# context manager

with lock:
  # access shared resource

# NOte: value only read without medify don't need to use lock


lock.acquire() with argument, default is True

if lock.acquire(False):
  lock acquired, do stuff
else:
  not acquire lock, do other
