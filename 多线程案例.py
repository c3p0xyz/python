import threading
lock = threading.Lock()
num = 100

def run(name):
    lock.acquire()
    global num
    if num > 0:
        num = num-1
        print(name,"窗口卖出一张票,还有",num,"张票")
    lock.release()
while True:
    if num > 0:
        t1 = threading.Thread(target=run,args=("A窗口",))
        t2 = threading.Thread(target=run,args=("B窗口",))

        t1.start()
        t2.start()
    else:
        break
print("票已售罄!")