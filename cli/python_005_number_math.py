# coding=utf-8
import math
import cmath
import operator
import random

a = -10.2
b = 3
print(abs(a))
print(math.ceil(a))   # ceil天花板,取上值
print(math.floor(a))  # floor地板，取下值

# print(cmp(a,b))
# cmp在python3中已经不可用了，以operator代替,需要导入operato模块
print (operator.lt(a, b))  # a<b    litter than
operator.le(a, b)          # a<=b   litter equal
operator.gt(a, b)          # a>b    greater than
operator.ge(a, b)          # a>=b   greater equal
operator.eq(a, b)          # a==b   equal
operator.ne(a, b)          # a!=b   not equal

print(max(a, b))
print(min(a, b))
print(round(a))

r = random.uniform(2, 6)  # 生成一个实数, 在[2,6]范围内
print(r)
print(int(r))
r = random.random()       # 生成一个实数，在[0，1）范围内
print(r)

A = 90                    # 角度
B = 1                     # 弧度
C = math.pi               # 符号pi
print(math.degrees(B))    # 弧度转换为角度，1弧度转换为角度为57.29角度
print(math.radians(A))    # 角度转换为弧度，90角度转换为弧度为1.57
print(math.degrees(C))    # pi转换为角度为180角度

print(dir(math))          # 把math包中的函数打印出来
print(dir(cmath))         # 把cmath包中的函数打印出来
