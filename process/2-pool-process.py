'''
class multiprocessing.Pool([num_processes[, initializer[, initargs[, maxtasksperchild]]]])

num_process: default is number of cpu cores
initializer: execute func once at start up, pickable not required
maxtaskperchild: default is None, mean process live as long as pool is alive, if set => after number of tasks process is killed and replaced with new worker process
'''
import multiprocessing

def do_work(data):
  return data**2

def start_process():
  print("starting", multiprocessing.current_process().name)

if __name__=="__main__":
  pool_size = multiprocessing.cpu_count() * 2
  pool = multiprocessing.Pool(processes=pool_size, initializer=start_process)

  inputs = list(range(10))
  outputs = pool.map(do_work, inputs)
  print('Outputs :', outputs)

  pool.close() # no more tasks
  pool.join() # wait for the worker processes to exit


'''
map_async(func, iterable[, chunksize[,callback]]) return AsyncResult

AsyncResult.get([timeout])

apply(func[, args[, kwargs]])
apply_async(func[, args[, kwargs[, callback[, error_callback]]]])

'''



from multiprocessing import Pool
import time

def multiply(x, y):
  return x * y


if __name__=='__main__':
  pool = Pool(processes=4)
  result = pool.apply_async(mult, (7,7)) # evaluate "multiply(7, 7)" asynchronously in a single process
  print(result.get()) # prints 49






