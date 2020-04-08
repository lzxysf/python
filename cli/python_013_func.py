# coding=utf-8

# 在python中，类型属于对象，变量是没有类型的
# [1,2,3]是list类型，‘hello’是字符串类型，而变量a是没有类型的
a = [1, 2, 3]
a = 'hello'

# 在python中numbers、strings、tuples是不可变类型,作为参数传给函数时是值传递，即复制后传递，不影响变量本身的数值
# 在python中lists、dicts是可变类型，作为参数传递给函数时是引用传递，即传递的是地址

x = 10
def a(x):
    x += 1                     # 值传递不会改变全局变量中的值
    print(x)
a(10)
print(x)

y = [1, 2, 3, 4]
def b(y):
    y.append([5, 6, 7, 8])      # 引用传递会改变全局变量中的值
    print(y)
b(y)
print(y)

def c(y):
    y = [5, 6, 7, 8]            # 但是引用传递直接修改了参数指向的地址，那么原地址的数据不会改变的
    print(y)
c(y)
print(y)


# 调用函数时可以使用的正式参数类型有：必须参数、关键字参数、默认参数、不定长参数
# 必须参数
def printme(str):
    print(str)
printme('hehe')

# 关键字参数
def printinfo(name, age):
    print('name is ' + name)
    print('age is ' + str(age))
printinfo(age = 12, name = 'alice')     # 使用关键字参数允许函数调用参数顺序与函数声明顺序不一致

# 默认参数，默认参数必须在普通参数后面
def printit(name, age = 22):
    print('name is ' + name)
    print('age is ' + str(age))
printit('shifu')

# 不定长参数
# 加了*号的参数会以元组的形式导入，存放所有未命名的变量参数
def printinfos(arg1, *vartuple):
    print("参数:")
    print(arg1)
    print(vartuple)
printinfos('apple', 1, 4)

# 不定长参数
# 加了**号的参数会以字典的形式导入
def printinfoss(arg1, **vardict):
    print("参数")
    print(arg1)
    print(vardict)
printinfoss('apple', a = 1, b = 2)

# 匿名函數
# python使用lambda来创建匿名函数
sum = lambda x, y: x + y
print(sum(3, 5))


total = 0 # 这是一个全局变量
def sum(arg1, arg2):
    total = arg1 + arg2
    print("这里的totoal是一个局部变量:" + str(total))
sum(10, 20)
print("这里的totoal是一个全局变量:" + str(total))

# 将内部作用域修改为外部作用域，使用global和nonlocal
num = 1
def fun1():
    global num      # 将局部变量修改为全局变量
    print(num)
    num = 123
    print(num)
fun1()
print(num)

def outer():
    num = 10
    def inner():
        nonlocal num    # 如果要修改嵌套作用域(外层非全局作用域)中的变量，需要nonlocal关键字
        num = 100
        print(num)
    inner()
    print(num)
outer()

# 可以通过 函数名.__doc__ 的方式来显示函数的说明文档
def add(a, b):
    "这是add函数文档"
    return a+b
print(add.__doc__)

# 不同于C的函数返回值只能返回一个，python的函数返回值可以返回多个
# 多个值以元组的方式返回
def fun(a, b):
    return a, b, a + b
print("函数的返回值"+str(fun(3,4)))
