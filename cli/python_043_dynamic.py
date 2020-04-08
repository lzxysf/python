# python是动态语言
# 动态语言是运行时可以改变其结构的语言
# C、C++是静态语言
import types

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{} is {} years old".format(name, age))
    def eat(self):
        print("i am eating")

p = Person('liming', 15) # liming is 15 years old

print(p.age) # 15

# 运行过程中给对象绑定（添加）属性
# 只会影响类的这个实例对象，不会对类对象本身和类创建的其它实例对象有影响
p.sex = 'male'
print(p.sex) # male
p1 = Person('laowang', 33) # laowang is 33 years old
# p1.sex    # 此句报错，在新创建的实例中，sex是没有被定义的


# 运行过程中给类绑定（添加）属性
# 这样就可以使所有的类的实例对象拥有这个属性
Person.sex = None
p = Person('xiaoli', 24) # xiaoli is 24 years old
print(p.sex)    # None

# 运行过程中给类绑定方法
# python中方法可以分为实例方法、静态方法、类方法
# 实例方法：需要绑定要一个对象上，第一个参数默认使用self，会把对象作为第一个参数传递进来
# 静态方法：使用装饰器@staticmethod进行定义，类和对象都可以调用，不需要默认参数
# 类方法：使用装饰器@classmethod进行定义，类和对象都可以调用，第一个参数默认使用cls，会把类作为第一个参数传递进来
print('-'*30)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{} is {} years old".format(name, age))
    def eat(self):
        print("i am eating")

# 定义实例方法
def run(self):
    print('I am running')

# 定义静态方法
@staticmethod
def testStatic():
    print('test static')

# 定义类方法
@classmethod
def testClass(cls):
    print('test class')

# 给对象动态添加实例方法
p = Person('xiaoq', 21)
p.run = types.MethodType(run, p)
p.run() # I am running

# 给类动态添加静态方法
Person.testStatic = testStatic
Person.testStatic() # test static

# 给类动态添加类方法
Person.testClass = testClass
Person.testClass() # test class


# 动态删除对象的属性或方法
# del 对象.属性
# delattr(对象, 属性)

del p.run
# p.run() # 删除run方法后执行会报错，找不到run