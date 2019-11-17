import threading

lock = threading.Lock()  # 创建一个线程锁

num = 100
def run(name):
    lock.acquire()  # 设置锁
    global num
    num = num-1
    print("线程",name,"正在执行,num=",num)
    lock.release()  # 释放锁

for i in range(100):
    t = threading.Thread(target=run,args=(i+1,))
    t.start()


# 全局解释器锁(GIL)
# 作用: 不管CPU数量是多少.都保证python程序中同一时间点只能执行一个线程. 这样做虽然保证了安全但是牺牲了CPU的
#        性能,弊大于利
# 解决办法: 使用多进程解决GIL所造成的问题