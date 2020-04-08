from multiprocessing import Process
import os
import time

'''
def run_proc(name):
    print("子进程运行中,name={},pid={}".format(name, os.getpid()))


if __name__=="__main__":

    print('父进程的pid:{}'.format(os.getpid()))
    p = Process(target=run_proc, args=('test',))
    p.start()
    p.join()
    print('父进程completed')
'''

# join方法用于等待子进程结束后再往下执行
# 建议子进程结束前，父进程不要结束，否则可能引发问题

# 设想如果没有join方法，且子进程是耗时的，但是父进程很快执行完毕了。当父进程结束，子进程未结束，子进程就会变成孤儿进程
# 在linux中孤儿进程会由init进程托管,这样会带来不确定性
# 不知道为什么明明父进程已经结束了，但是现象是未结束，ps -ef也显示未结束
# 因此我使用了kill -9强制结束了父进程
# 现在知道了，Process中父进程先运行完毕不会立即结束，会等待子进程运行完毕后一起结束
# 但是fork和下面的pool，父进程如果先运行完毕就会立即结束，子进程就会变成孤儿进程或和父进程一起结束

'''
def run_proc():
    time.sleep(100)
    print("子进程运行中,其父进程pid为{}".format(os.getppid()))

p = Process(target=run_proc)
p.start()
print('父进程{}completed'.format(os.getpid()))
'''

'''
Process([group [, target [, name [, args [, kwargs]]]]])

target：表示这个进程实例所调用对象

args：表示调用对象的位置参数元组

kwargs：表示调用对象的关键字参数字典

name：为当前进程实例的别名

group：大多数情况下用不到
'''

'''
Process类常用方法：

is_alive()：判断进程实例是否还在执行

join([timeout])：是否等待进程实例执行结束，或等待多少秒

start()：启动进程实例（创建子进程）

run()：如果没有给定target参数，对这个对象调用start()方法时，就将执行对象中的run()方法

terminate()：不管任务是否完成，立即终止
'''

'''
Process类常用属性：

name：当前进程实例别名，默认为Process-N，N为从1开始递增的整数

pid：当前进程实例的PID值
'''

# 进程的创建-Process子类
# 如果重写__init__方法，那么必须要调用父类的构造方法Process.__init__(self)
class MediaProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name
        self.i = 0
    
    def run(self):
        while True:
            print('{}子类运行中{}'.format(self.name, self.i))
            time.sleep(1)
            self.i+=1

p = MediaProcess('media-process')
p.start()
p.join()
