"""
python的queue模块实现了同步的，线程安全的队列类,包含Queue,LifoQueue,PriorityQueue
queue.Queue()
Queue是构造方法，函数签名Queue(maxsize),其中maxsize设置队列的大小
如果不填写maxsize就是无限大，只要内存没有限制
Queue.qsize()  返回队列的大小
Queue.empty()  如果队列为空，返回True，否则返回False
Queue.full()  如果队列满了，返回True，否则返回False
Queue.full与maxsize大小对应
Queue.put(item, block=True, timeout=None) 在队列尾部插入数据item,如果此时队列已经满了且block=False直接报Full错误，队列满了且block=True就等待，              timeout必须是None、0、正数n，None为一直等，0为不等，正数n为等待n秒，若还不能存入，报Full异常
Queue.put_nowait(item)  往对列里存放元素，不等待，放不进值会抛出异常
Queue.get(block=True, timeout=None)  从队列里取元素,如果此时队列为空且block=False直接报empty错误，队列为空且block=True就等待，timeout必须是None、0、正数n，None为一直等，0为不等，正数n为等待n秒，若还不能获取，报empty异常
Queue.get_nowait()  从队列里取元素，不等待,取不到值会抛出异常
Queue.task_done()  表示队列中某个元素被消费后，手动调用taskdone函数。主要是给join用的，每次get后需要调用task_done，直到所有任务都task_done。
join才取消阻塞
Queue.join()  一直阻塞直到队列中的所有元素都被取出
"""
import queue
import threading
import time

# 创建消息队列
# 3，表示消息队列最大的个数
queue1 = queue.Queue(3)
# 放入数据
queue1.put(123)
queue1.put('abc')
queue1.put(['banana','juice'])

# 队列满了，直接调用put默认为一直等待
# queue1.put(456)

# 队列满了，执行此方法1秒后，会抛出Full异常
try:
    queue1.put(456,block=True,timeout=1)
except queue.Full:
    print('队列满了')

result = queue1.full()
print(result)

# 查看队列的个数
size = queue1.qsize()
print(size)
# 获取队列的数据
value = queue1.get()
print('取出队列的数据：' + str(value))
size = queue1.qsize()
print('剩余队列的个数：' + str(size))
# 获取队列的数据
value = queue1.get()
print('取出队列的数据：' + str(value))
size = queue1.qsize()
print('剩余队列的个数：' + str(size))
# 获取队列的数据
value = queue1.get()
print('取出队列的数据：' + str(value))
size = queue1.qsize()
print('剩余队列的个数：' + str(size))


# 队列为空时，使用get会等待，直到队列有数据再取值
# value = queue1.get()


"""
下面是一个队列应用的例子
"""


class MyThread(threading.Thread):
    def run(self):
      while True:
          process_queue()


myqueue = queue.Queue(10)

def process_queue():
    value = myqueue.get()
    time.sleep(0.5)
    print('取出的数据为：', end='')
    print(value)

thread1 = MyThread()
thread1.start()

while True:
    value = input('请输入要向队列中添加的字符串')
    myqueue.put(value, block=True, timeout=1)
    time.sleep(1)
