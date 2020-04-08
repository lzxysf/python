import sys
from sys import argv,path # 注意此时argv和path已经成为上下文中的变量，注意不要和其他变量冲突

print(sys.argv)
print(sys.path)

print(argv)
print(path)

# 内置的函数dir可以找到模块内定义的所有名称，以一个字符串列表的形式返回
print(dir(sys))
