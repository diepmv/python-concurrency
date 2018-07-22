asyncio.get_event_loop()

AbstractEventLoop.run_forever()
AbstractEventLoop.stop()
AbstractEventLoop.close()


AbstractEventLoop.run_util_complete(future)
'''
Cooperative multitasking
Task suspend themself to allow others run
Event loop resumes the task when IO operation complete
tasks => coroutines

'''
