# 输入dir(__builtins__), 可以看到很多python解释器启动后默认加载的属性和函数，这些函数称之为内建函数

# help() 函数用于查看函数或模块用途的详细说明
# 此方法会直接打印，不需要用print
# help('sys')

# setattr用于设置属性值，该属性不一定是存在的
# setattr(obj, name, default)
# getattr用于获取属性值，不存在会AttributeError报错
# getattr(obj, name[, default])
# 当有default参数时，不存在name值不会报错，会自动返回default值
# hasattr(obj, name) 判断是否有此属性


class A:
    bar = 1


a = A()
value = getattr(a, 'bar')
print(value)
setattr(a, 'book', 3)
value = getattr(a, 'book')
print(value)


# all(iterable)
# 函数用于判断给定的可迭代参数iterable中所有元素是否都为True，如果是返回True，如果不是返回False
# 元素除了0、空、None、False其它都是True
# any(iterable)
# 和all相反

value = all(['a', 'b', 'c'])      # 列表全部不为False
print(value)
value = all((1, 0, 2, 4))         # 元组有一个为0
print(value)
value = all(['e', 'b', ''])         # 列表有一个为''
print(value)

print(all([]))                    # 空列表和空元组都为True
print(all(()))                    # 空列表和空元组都为True


# dir()不带参数时，返回当前范围内的变量、方法和定义的类型列表
# dir()带参数时，返回参数属性、方法列表
print(dir())
print(dir([]))

# slice(stop)                   [:stop]
# slice(start, stop)            [start:stop]
# slice(start, stop, step)      [start:stop:step]
myslice = slice(2,5)
arr = [1, 2, 3, 4, 5, 6, 7]
print(arr[myslice])

# divmod(a,b) 返回一个包含商和余数的元组(a//b,a%b)
value = divmod(5, 2)
print(value)
value = divmod(13, 5)
print(value)

# id(object)获取对象的内存地址
a = 'google'
print(id(a))
b = 1
print(id(b))

# sorted()函数对所有可迭代的对象进行排序操作
# sorted()默认是升序的
'''
sort与sorted的区别：
sort是list的方法，sorted可以对所有可迭代的对象进行排序操作
list的sort方法是对列表本身进行修改，内建函数sorted是返回一个新的list,而不是在原来的基础上进行操作
list的sort方法效率稍高
'''
arr = [1, 5, 88, 2, 9, 12]
arr.sort()
print(arr)

print(sorted(arr))                  # 默认升序

print(sorted(arr, reverse=True))    # 降序

# enumerate()函数用于将一个可遍历的数据对象组合成一个索引序列，同时列出数据下标和数据，主要用于for循环
# enumerate(sequence,[start=0])
# 参数sequence--支持迭代的对象
# 参数start--下标起始位置
# 返回值==enumerate(枚举)对象
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
value = enumerate(seasons, start=1)
print(list(value))

for i, element in enumerate(seasons):
    print(i, element)

# input()返回一个string类型

# staticmethod静态方法


class C():
    @staticmethod
    def f():
        print('baidu')


C.f()               # 静态方法无需实例化
C().f()             # 也可以实例化后调用


# eval函数用来执行一个字符串表达式，并返回表达式的值
value = eval('2**10')
print(value)
# eval可以直接提取用户输入的多个值，其实是eval将其转换为了元组
# i,j = eval(input('输入多个值'))
# print(i,j)


# int用于将字符串或数字转换成整型，可以以16进制、8进制输入
# class int(x[,base=10]) 默认为十进制输入，当有base参数时，数值x必须以字符串形式输入
value = int('10', 8)
print(value)

# exec动态执行python代码，也就是说exec可以执行复杂的python代码，而不是像eval一样只能计算表达式的值
# eval()函数和exec()函数的区别
# eval()函数只能计算单个表达式，而exec()函数可以动态运行代码段
# eval()函数可以有返回值，而exec()函数的返回值永远为None
'''
eval(object[, globals[, locals]])
exec(object[, globals[, locals]])
object--必选参数，表示要被执行的Python代码
globals--可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象
locals--可选参数，标识局部命名空间（存放局部变量），如果被提供，可以是任何映射对象
'''

expr = """
def init(a, b, c):
    sum = a + b + c
sum = init(a,b,c)
print(sum)
"""
exec(expr, {'a': 3, 'b': 5, 'c': 11})

# filter函数用于过滤序列
# filter(function, iterable)
# filter返回一个迭代器对象，如果要转换成列表，使用list()转换


def isodd(n):
    if n % 2 == 0:
        return True
    else:
        return False


tmplist = filter(isodd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11])
print(list(tmplist))

# map会根据提供的函数对指定的序列做映射
# map(function, iterable,...)
# function--函数
# iteralbe--一个或多个序列
# 返回值--python2返回列表，python3返回迭代器


def square(x):
    return x*x


tmp = map(square, [1, 3, 5, 8])
print('map例子1', list(tmp))
tmp = map(lambda x: x * x, [1, 3, 5, 9])
print('map例子2', list(tmp))
tmp = map(lambda x, y: x * y, [1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
print('map例子3', list(tmp))

# frozenset 冻结的集合，不可变集合
# frozenset(iterable)

a = frozenset([1, 2, 3])
print(a)

# globals函数会以字典的形式返回当前位置的所有全局变量
print(globals())

# locals函数会以字典的形式返回当前位置所有局部变量
print(locals())

# hash(object)用于获取一个对象的哈希值
# hash函数可以用于数字、字符串和对象，不能直接应用于列表、元组、字典，此时将其转换成str传入hash函数
str1 = 'hello world'
str2 = 'hello world'
str3 = str2 + ''
print(hash(str1))
print(hash(str2))


# isinstance()判断一个对象是否是一个已知的类型
'''
isinstance和type的区别：
type不会认为子类是一种父类类型，不考虑继承关系
isinstance会认为子类是一种父类类型，考虑继承关系
如果要判断两个类型是否相同，推荐使用isinstance
'''
a = 1
print(isinstance(a, int))
b = 'heb'
print(isinstance(b, str))
print(isinstance(b, int))
print(isinstance(b, (int, str, list)))


class A:
    pass


class B(A):
    pass


a = A()
b = B()
print(isinstance(a, A))
print(isinstance(b, A))

# issubclass
# 判断是否是子类
print(issubclass(B, A))

# len(s)返回对象长度或项目个数
a = 'hello'
print(len(a))
b = [1, 5, 9, 33]
print(len(b))

# memoryview
v = memoryview(bytearray('hello', 'utf-8'))
print(v[1])
print(v[-1])
print(v[1:4])
print(v[1:4].tobytes())


# print方法用于打印输出
# 在python2中print是一个关键字，在python3中print是一个函数
# print(*objects,sep=' ',end='\n',file=sys.stdout)
# objects--表示一次可以输出多个对象，输出多个对象时，可以用‘,’隔开
# sep--输出多个对象时的间隔，默认为空格
# end--用来设定以什么结尾，默认为'\n'，可以改成其他字符
# file--要写入的文件对象
a = 1
b = 'hello'
print(a, b)
print('www', 'baidu', 'com', sep='.')

# range(start,stop,step)
# 从start开始到stop结束，不包括step
# range(stop) 相当于range(0,stop)
# step步长，默认为1
# 返回值，python3返回的是对象迭代器，python2返回的是列表
print(list(range(10)))
print(list(range(0, 10)))
print(list(range(0, -10, -1)))

# reversed(seq)
# seq--要转换的序列，可以是list、tuple、string、range
# 返回值--对象迭代器
print(list(reversed(range(10))))

# vars(object) 函数返回对象object的属性和属性值的字典对象


class A:
    age = 1


print(vars(A))

# __import__()函数用于动态加载类和函数
# 如果一个模块经常变化，就应该使用这个函数
