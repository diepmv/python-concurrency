import threading


semaphore = threading.Semaphore()
# internal counter

semaphore.acquire() #decrements the counter
# access the shared resource
semaphore.release() #increments the counter
