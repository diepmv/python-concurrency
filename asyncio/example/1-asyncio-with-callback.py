import asyncio

loop = asyncio.get_event_loop()

def hello():
  print("Hello")
  loop.call_later(3, print_world)


def print_world():
  print("world")


if __name__=="__main__":
  loop.call_soon(hello)
  loop.run_forever()
