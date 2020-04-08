# 进程间通信有多种方式，其中就可以通过Queue进行进程间通信
# 使用的模块是multiprocessing.Queue
# queue.Queue和multiprocessing.Queue的区别
# 前者是进程内队列消息通信，后者是进程间通信

# 用法和028中queue.Queue的用法基本一致
# 使用时导入from multiprocessing import Queue
# 然后创建Queue实例，传入进程函数即可

# 但是如果Queue用于Pool创建的多进程之间传递消息却有不同的地方
# 如果使用Pool创建进程，就需要使用multiprocessing.Manager而不是multiprocessing.Queue
from multiprocessing import Manager

q = Manager().Queue()

# 然后在pool.apply_async(func,(q,))中将q传入进程处理函数即可
