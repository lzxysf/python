# 一个线程使用自己的局部变量比使用全局变量要好
# 因为局部变量只有自己的线程能看见，不影响其它线程，而全局变量的修改必须加锁
# 但是使用局部变量也有问题，就是在函数调用时，传递起来很麻烦
# 这时应该使用ThreadLocal

# 一个ThreadLocal对象虽然是全局变量，但是每个线程只能读写自己的独立副本，互不干扰

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('dongGe',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('老王',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
