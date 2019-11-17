from multiprocessing import Process
import time

def run(name):
    print("进程",name,"正在执行!")
    time.sleep(5)

if __name__ == '__main__':
    p1 = Process(target=run,args=("p1",))   # 创建进程
    p2 = Process(target=run,args=("p2",))
    p3 = Process(target=run,args=("p3",))
    p4 = Process(target=run,args=("p4",))
    p5 = Process(target=run,args=("p5",))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()