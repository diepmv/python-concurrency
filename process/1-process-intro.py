import multiprocessing

def do_some_work(val):
  print("Doing some work in thread")
  print("echo:{}".format(val))
  return

if __name__=="__main__":
  val = "text"
  t = multiprocessing.Process(target=do_some_work, args=(val,))
  t.start()
  j.join()


# Note:

# class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, daemon=None)

# is_alive()
# terminate()
