'''
multiprocess.Value
multiprocess.Array
'''

# create value object
# multiprocessing.Value(typecode_or_type, *args[, lock])

counter = Value('i') # shared object of type int, defaults to 0

is_running = Value(ctypes.c_bool, False, lock=False) # shared object of type boolean, defaulting to False, unsynchronized

my_lock = multiprocessing.Lock()

size_counter = Value('I', O, lock=my_lock) # shared object of type long, with a lock specified
