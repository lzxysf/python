# 一个简单的类
# 类中的方法，第一个参数都是self，self代表类的实例，而非类
# self可以用任何名字的参数代替，但是习惯用self。只要是类中方法的第一个参数即代表类的实例的意思
print('一个简单的类'.center(30, '*'))


class MyClass:
    i = 12345

    def f(self):
        return 'hello world'


x = MyClass()
print(x.i)
print(x.f())


# python类中__init__是构造方法
# python类中__str__类似于java中的toString方法
print('构造方法'.center(30, '*'))


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{}的年龄是{}'.format(self.name, self.age)


people = People('小明', 25)
print(people)


# self代表了类的实例而非类
class Test:
    def test(self):
        print(self)
        print(self.__class__)


x = Test()
x.test()

# 类的方法
# 在类的内部，使用def关键字来定义一个方法，与一般的函数定义不同，类方法必须包含一个self参数，且是第一个参数，self代表的是类的实例


class human:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接访问
    __weight = 0

    def __init__(self, name, age, __weight):
        self.name = name
        self.age = age
        self.__weight = __weight

    def speak(self):
        print('{} say i am {} years old!'.format(self.name, self.age))


x = human('lsf', 26, 155)
x.speak()


# python支持类的继承，在圆括号中的是父类（基类）
class student(human):
    grade = 0

    def __init__(self, name, age, weight, grade):
        # 调用父类的构造函数
        human.__init__(self, name, age, weight)
        self.grade = grade

    # 重写父类的方法
    def speak(self):
        print('{} say i am {} years old, my grade is {}'.format(
                    self.name, self.age, self.grade))


x = student('lsf', 26, 155, 100)
x.speak()


'''
python同样支持多继承
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
要注意圆括号中父类的顺序，若在父类中有相同的方法名，而在子类使用时未指定，python从左向右搜索此方法
'''

'''
__new__方法----主要是实现自定义类以及自定义metaclass
__init__方法----用于初始化python对象
__del__方法----用于销毁python对象
'''

'''
class A:

    bar = 0 # 类所有的实例共用此变量

    #实例方法
    def show(self):
        print('hello')

    #静态方法
    @staticmethod
    def teststatic():
        pass
    
    #类方法
    @classmethod
    def testclass(cls):
        print(cls.bar)
        cls().show()

A.teststatic() # 静态方法的调用不需要实例化
A.testclass() # 类方法的调用不需要实例化
'''

'''
class foo:
    pass

a = foo()
b = a

del a  # 此时引用计数为1，不会调用foo类的__del__方法
del b  # 此时引用计数为2，调用foo类的__del__方法

Python 采用自动引用计数（ARC）方式来回收对象所占用的空间，当程序中有一个变量引用该 Python 对象时，Python 会自动保证该对象引用计数为 1；当程序中有两个变量引用该 Python 对象时，Python 会自动保证该对象引用计数为 2，依此类推，如果一个对象的引用计数变成了 0，则说明程序中不再有变量引用该对象，表明程序不再需要该对象，因此 Python 就会回收该对象,此时会调用类的__del__方法。
'''