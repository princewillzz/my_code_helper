import threading
from time import sleep
def hello():
    for _ in range(10):
        print("hello")

def hii():
    for _ in range(10):
        print("hii")

x = threading.Thread(target=hello)
y = threading.Thread(target=hii)

x.start()
y.start()

print(threading.activeCount())


