'''
An object that acts as proxy for a result that is yet to be computed,
main thread submit task to actor, which may be thread, process, or OS func and continue execution until it need result from execution or until execution is complete
future object enables asynchronous programming, executor represent actor

'''

future = executor.submit(func, args)
# do other thing
result = future.result() # if func is not complete => block or until timeout


# future methods

future.cancel() # attempt to cancel execution, return True if successful

future.done() # return TRue if completed or canceled

future.exception(timeout=None) # return the exception raised, if any

future.add_done_callback(fn) # attaches function to be called on completeion or cancellation



concurrent.futures.wait(fs, timeout=None, return_when=ALL_COMPLETED)

concurrent.futures.as_complete(fs, timeout=None)
