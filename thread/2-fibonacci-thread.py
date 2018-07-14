import threading

class FibonacciThread(threading.Thread):
  # Thead.__init__() always called first
  def __init__(self, num):
    Thread.__init__(self):
    self.num = num

  def run(self):
    fib = [0] * (self.num + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, self.num+1):
      fib[i] = fib[i-1] + fib[i-2]
      print fib[self.num]


myFibTask1 = FibonacciThead(9)
myFibTask2 = FibonacciThead(12)

myFibTask1.start()
myFibTask2.start()


myFibTask1.join()
myFibTask2.join()


