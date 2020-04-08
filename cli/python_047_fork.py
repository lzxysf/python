import os

# fork炸弹
# while True:
#     os.fork()

# fork函数只可以在UNIX/LINUX/MAC上运行，无法在Windows上运行
# fork函数执行后，会分化出一个子进程，从此句后继续执行，子进程的环境变量和父进程相同，当然ret值是不一样的
# 父进程，也就是当前进程，ret值是它创建的子进程的pid
# 子进程中ret值为0
ret = os.fork()


# os.getpid--获得当前进程的pid
# os.getppid--获得当前进程的父进程的pid
if ret == 0:
    print('子进程中执行,子进程的pid是{},其父进程pid{}'.format(os.getpid(), os.getppid()))
else:
    print('父进程中执行,父进程的pid是{},其子进程pid{}'.format(os.getpid(), ret))


# 多次fork问题
# 程序中调用几次fork即进行多少次分裂

# 父进程、子进程的执行顺序没有规律，完全取决于调度算法
