from twisted.internet import reactor


def hello():
  print("Hello")

  reactor.callLater(3, print_world)

def print_world():
  print("World!")

if __name__=="__main__":
  reactor.callWhenRunning(hello)
  reactor.run()
