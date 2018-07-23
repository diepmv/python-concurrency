from gevent import sleep

def hello():
  print("Hello")
  sleep(3)
  print(world)

if __name__=="__main__":
  hello()
