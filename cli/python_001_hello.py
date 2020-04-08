# coding=utf-8
print ("hello world")
print ("-"*10)
print ('123'+'abc')
print ('你好世界')

# 读取外部输入，input读进去的都是字符串，需要别的类型的话自己转化
name = input('输入你的姓名')
age = input('输入你的年龄')
age = int(age)+1
print('your name is '+name)
print('your age is '+str(age))


# python中空函数会报错，此时可以用占位符pass占位置


def func1():
    pass
