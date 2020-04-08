import _thread
import time

# python3通过两个标准库_thread和threading提供对线程的支持
# _thread提供了对低级别的、原始的线程以及一个简单的锁，它相比于threading的功能还是有限的
# threading中除了提供_thread的功能外，还包含以下功能，见下一个文件

# 为线程定义一个函数


def print_time(threadname, delay):
    while True:
        print('{},{}'.format(threadname, time.ctime(time.time())))
        time.sleep(delay)


# 创建两个线程
try:
    _thread.start_new_thread(print_time, ('Thread-1', 2))
    _thread.start_new_thread(print_time, ('Thread-2', 3))
except Exception:
    print('无法启动线程')

while 1:
    pass
