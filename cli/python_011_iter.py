# coding=utf-8
# 迭代器，迭代是python最强大的功能之一,是访问集合元素的一种方式
# 迭代器有两个基本方法,iter()和next()
import sys
from collections import Iterable,Iterator

arr = [1, 2, 3, 4]
it1 = iter(arr)
print(next(it1))
print(next(it1))

dict1 = {'0': 'zero', '1':'one', '2':'two', '3':'three'}
it2 = iter(dict1)
for i in it2:
    print(i)

arr2 = [3, 4, 5, 6]
it3 = iter(arr2)
it4 = iter(arr2)

for i in it3:
    print(i)

while True:
    try:
        print(next(it4))
    except StopIteration:
        break

# 列表、元组、字典、字符串都是可迭代对象，但不是迭代器，要想变成迭代器，需要使用iter进行转换
# 凡是可用作for循环的都是Iterable类型
# 凡是可作用于next函数的对象都是Iterator类型
# Iterable指的是可迭代的，Iterator指的是迭代器
# 所有的生成器都是迭代器
print(isinstance([],Iterable)) # True
print(isinstance((),Iterable)) # True
print(isinstance({},Iterable)) # True

print(isinstance([],Iterator)) # False
print(isinstance((),Iterator)) # False
print(isinstance({},Iterator)) # False
