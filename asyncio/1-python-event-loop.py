asyncio.get_event_loop()

AbstractEventLoop.run_forever()
AbstractEventLoop.stop()

# stop loop before close, close non-running loop
AbstractEventLoop.close()


AbstractEventLoop.run_util_complete(future)
'''
+Cooperative multitasking:
_Task suspend themself to allow others run
_Event loop resumes the task when IO operation complete
_tasks => coroutines

'''
