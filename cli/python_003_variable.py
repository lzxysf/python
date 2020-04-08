# coding=utf-8
# python的数据类型：数字、字符串、复数，列表、元组、字典
import json

a = b = c = 1
a, b, c = 1, 3.4, 'alice'

s = "hello world!"
x = '你好'
print(s[1:7])  # 前包含后不包含
print(s[1:])
print(s[-1:-5])  # 倒着数时候是前不包含后包含
print(s[:-1])
print(s+x)
print(x*2)

# 列表可以包含数字、字符串、另一个列表
# 列表用[]表示，元素之间用,隔开
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
print (list)               # 输出完整列表
print (list[0])            # 输出列表的第一个元素
print (list[1:3])          # 输出第二个至第三个元素
print (list[2:])           # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2)       # 输出列表两次
print (list + tinylist)    # 打印组合的列表

# 元组和列表基本类似
# 元组用()表示，元素之间用,隔开
# 元组和列表的区别是元组不能二次赋值，相当于只读列表
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print (tuple)               # 输出完整元组
print (tuple[0])            # 输出元组的第一个元素
print (tuple[1:3])          # 输出第二个至第三个的元素
print (tuple[2:])           # 输出从第三个开始至列表末尾的所有元素
print (tinytuple * 2)       # 输出元组两次
print (tuple + tinytuple)   # 打印组合的元组

# 列表是有序的对象集合，字典是无序的对象集合
# 字典用{}表示，以key-value的形式存储
# key值在[]中而不是()中
dict = {}
dict['one'] = 'this is one'
dict[2] = 'i am john'
print(dict)

dict = {'1': 'apple', '星期': '明天', 'pic1': 1}
print(dict['1'])
print(dict['星期'])
print(dict.keys())
print(dict.values())
print(dict)
# print (json.dumps(dict, encoding="UTF-8", ensure_ascii=False))

a = 11
b = 2
print(a**b)
print(a//b)

a = 1
b = 0
if a:
    print('true')
if a and b:
    print('true')
else:
    print('false')

if (a or b):
    print('true')

if not(a and b):
    print('true')

a = 12345
b = 12345
c = 20
list = [10, 2, 3, 4, 5 ]

if a in list:
    print ('true')
if b not in list:
    print('true')

# is和is not判断的是变量的内存地址是否相同
# python中两个相等的比较简单的变量指向了同一块内存地址
# 但是如果数据类型不一样，就不会指向同一块内存地址了，a=10,b=10.0时，a is not b
if a is b:
    print('a is b')

if a is not c:
    print('a is not c')

# id可以获取一个变量的地址
print (id(a))
print (id(b))

# 如下，虽然y和z都和x的值相等，但是y是引用，直接指向了x的地址，z是复制，地址和x不一样
x = [1, 2, 3, 4, 5]
y = x
z = x[:]
print(id(x))
print(id(y))
print(id(z))

# python不支持++和--这种语法，因为python中的数值和字符串都是不可变对象，对不可变对象操作都会生成一个新的对象
# 而++和--都是对该对象的内存直接加一或减一
