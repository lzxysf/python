# coding=utf-8
import os

print('这是alice\'的问候')
print('这将直接执行'+os.getcwd())

for i in range(10):
    print(i)


def fun(arg1, arg2):
    result = arg1 + arg2
    print('%d+%d=%d'%(arg1, arg2, result))
    return result


fun(1, 2)