# coding=utf-8

# 不一下子创建一个序列，而是一边循环一边计算来生成序列，因此可以节省内存
# 在python中这种一边循环一边计算的机制叫做生成器
# 生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解，生成器就是一个迭代器


# 创建生成器的方法1
# 第一种方法就是把一个列表生成式的[]改成()
L = [x for x in range(5)] # 列表生成式
print(L)
G = (x for x in range(5)) # 生成器
print(next(G)) # 0
print(next(G)) # 1
print(next(G)) # 2
print(next(G)) # 3
print(next(G)) # 4
# print(next(G)) # 执行此句报StopIteration异常
# 生成器保存的是算法，每次调用next都是在计算下一个元素的值
print('-'*30)
# 生成器就是迭代器，而迭代器也必然是可迭代的，实际不会通过next计算，太麻烦了，一般通过for进行遍历
G = (x*2 for x in range(5))
for i in G:
    print(i)
print('-'*30)


# 创建生成器的方法2
# 在python中，使用了yield的函数被称为生成器generator
# 以下实例为使用yield实现斐波那契数列
import sys

def fabonacci(n):               # 生成器函数，斐波那契
    a, b, counter = 1, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a+b
        counter += 1


f = fabonacci(10)               # f是一个迭代器，由生成器返回生成

# while True:
#     try:
#         print(next(f))
#     except StopIteration:
#         break

for x in f:
    print(x)

