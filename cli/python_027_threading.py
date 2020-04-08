import threading
import time

'''
threading.currentThread:返回当前的线程变量
threading.enumerate:返回一个当前正在运行的线程的list
threading.activeCount:返回正在运行的线程的数量，与len(threading.enumerate)有相同的结果

Thread类的方法
run()           用以表示线程活动的方法
start()         启动线程活动
join([time])    等待线程终止
isAlive()       返回线程是否活动
getName()       返回线程名称
setName()       设置线程名称
'''

def say():
    print('hello world')
thread1 = threading.Thread(target=say)
# thread1.start()


class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        while True:
            print('{},{}'.format(self.name, time.ctime(time.time())))
            time.sleep(self.delay)


thread1 = myThread(1, 'Thread-1', 2)
thread2 = myThread(2, 'Thread-2', 3)

# thread1.start()
# thread2.start()


# 如果多个线程同时对某个数据修改，则可能出现不可预料的后果，为了保证数据的正确性，需要对线程进行同步
# 使用Thread对象的Lock可以实现简单的线程同步，这两个对象都有acquire方法和release方法，对于那些需要每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间
# 一次只允许一个线程获得锁
# 注意acquire后必须release,否则这个线程执行完后，其它线程就会一直等待，无法获得锁以继续
# 下面的例子中，预计g_num的值最终为2000000，但是执行过程中出现了脏读，因此需要进行同步
g_num = 0

def test1():
    global g_num
    # threadlock.acquire()
    for i in range(1000000):
        g_num += 1
    # threadlock.release()

def test2():
    global g_num
    # threadlock.acquire()
    for i in range(1000000):
        g_num += 1
    # threadlock.release()

threadlock = threading.Lock()

t1 = threading.Thread(target=test1)
t2 = threading.Thread(target=test2)

t1.start()
t2.start()
t1.join()
t2.join()

print('g_num的值为{}'.format(g_num))


# 死锁
# https://blog.csdn.net/u013210620/article/details/78723704
# 所谓死锁，是指两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，若无外力作用，它们都将无法推进下去
# 死锁的结构一般都是这样的，即在一个线程中锁A中套着锁B，然后另一个线程中锁B套着锁A
