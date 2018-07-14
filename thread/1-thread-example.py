import threading

def do_some_work(val):
  print("Doing some work in thread")
  print("echo: {}".format(val))
  return 

val = "text"

t = threading.Thread(target=do_some_work, args=(val,))
t.start()
t.join()


# Note
'''
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, daemon=None)
'''
