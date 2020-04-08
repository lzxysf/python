'''
为了更好使用协程来完成多任务，python中的greenlet模块对其封装，从而使得切换任务变的更加简单
'''
from  greenlet import greenlet
import time

def test1():
    while True:
        print('----A----')
        time.sleep(0.5)
        gr2.switch()

def test2():
    while True:
        print('----B----')
        time.sleep(0.5)
        gr1.switch()

gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()
