'''
A manager controls a server process, which maintain object that
can be shared amongst other process, example of shared object: Value, Array, Dict, List, Lock, Semaphore. processes access those shared objects do so using proxy=> slower than shared memory, but can share much more complex type than just Value or Array, can shared across network.
'''

# create a manager object
# multiprocessing.Manager() spins up a new process

import multiprocessing

def do_work(dictionary, item):
  dictionary[item] = item ** 2


if __name__=="__main__":
  mgr = multiprocessing.Manager()
  d = mgr.dict()

  jobs = [multiprocessing.Process(target=do_work, args=(d, i)) for i in range(8)]

  for j in jobs:
    j.start()
  for j in jobs:
    j.join()
  print('Results:', d)
