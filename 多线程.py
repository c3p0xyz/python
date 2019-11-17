import threading
import time

def run(name):
    print(name,"线程执行完成!")
    time.sleep(5)

# 程序执行时,程序本身就是一个线程,叫主线程
# 手动创建的线程,叫子线程
#　主线程在执行中不会等待子线程执行完毕，会直接执行

t1 = threading.Thread(target=run,args=("T1",))  #　逗号不能少
t2 = threading.Thread(target=run,args=("T2",))

t1.start()  # 开启线程
t2.start()

t1.join()   # 等待子线程执行完成再执行主线程
t2.join()

print("执行结束了!!!")