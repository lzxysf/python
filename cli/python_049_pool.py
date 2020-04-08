'''
进程池
初始化Pool时，可以指定一个最大进程数
当有新的进程任务提交到Pool时，如果进程池还没有满，那么就会在空闲进程中执行该任务，如果进程池满了，就会等待进程池有空闲位置后再执行该进程
'''
from multiprocessing import Pool


def proc_msg(msg):
    print('进程处理的数据msg为{}'.format(msg))


pool = Pool(3)

for i in range(10):
    pool.apply_async(proc_msg, (i,))

pool.close()  # 关闭进程池，关闭后pool不再接受新的请求
pool.join()   # 等待pool中所有子进程执行完毕，必须放在所有close进程之后
# 如果不调用pool.join(),父进程执行完毕后，子进程也会跟着完蛋，此时要想正常执行，父进程不能结束，可以循环，如下

# while True:
#     pass

'''
multiprocessing.Pool常用函数解析：

apply_async(func[, args[, kwds]]) ：使用非阻塞方式调用func（并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程,
args为传递给func的参数列表，kwds为传递给func的关键字参数列表
注解：使用此方法，一直向pool中添加进程任务也不会阻塞，进程会在进程池排队等待被处理

apply(func[, args[, kwds]])：使用阻塞方式调用func
注解：使用此方法，会被阻塞。即使进程池没有满，使用此方法提交一个进程任务后，该方法会一直阻塞到该进程执行完毕

close()：关闭Pool，使其不再接受新的任务

terminate()：不管任务是否完成，立即终止

join()：主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用

'''
