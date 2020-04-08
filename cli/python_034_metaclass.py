# python中类也是对象
# 因此可以：
# 将类赋值给一个变量
# 拷贝它
# 增加它的属性
# 将它作为函数参数进行传递


# 动态创建类
def choose_class(name):
    if name == 'foo':
        class Foo:
            pass
        return Foo
    else:
        class Bar:
            pass
        return Bar


Myclass = choose_class('foo')  # 动态创建类
myclass = Myclass()           # 创建类的实例

# 使用type动态创建类
# type可以用作查看一个对象的类型
# type还有完全不同的功能，动态创建类

print(type(myclass))  # 结果是Myclass，即类实例myclass的类型为类Myclass
print(type(Myclass))  # 结果是type,也就是说类对象本身的类型是type


# 用class创建一个类
class Test:
    pass


# 用type创建一个类
Test2 = type("Test2", (), {})


# 用type创建一个带有属性的类
Test3 = type("Test3", (), {'bar': True})


# 用type创建一个继承父类的类
Test5 = type("Test5", (Test3,), {})
test5 = Test5()
print(test5.bar)


# 用type创建一个带有实例方法的类
def echobar(self):
    print('bar')


Test6 = type("Test6", (), {'echobar': echobar})
test6 = Test6()
test6.echobar()


# 用type创建一个带有静态方法的类

@staticmethod
def testStatic():
    print('teststatic')


Test7 = type('Test7', (), {'testStatic': testStatic})
test7 = Test7()
test7.testStatic()


# 用type创建一个带类方法的类
@classmethod
def testClass(cls):
    print('testClass')


Test8 = type('Test8', (), {'testClass': testClass})
test8 = Test8()
test8.testClass()


# 用type创建一个类
Test9 = type('Test9', (Test3,), {'echobar': echobar, 'testStatic': testStatic, 'testClass': testClass})


# type就是元类
# 元类就是用来创建类的类，元类就是类的类
# python中所有的东西都是对象，这包括整数、字符串、函数以及类

# 使用class创建类的时候，可以使用__new__方法来
# 1.拦截类的创建
# 2.修改类
# 3.返回修改之后的类
# __new__方法比__init__方法更早地被执行
#  def __new__(cls, future_class_name, future_class_parents, future_class_attr)

'''
“元类就是深度的魔法，99%的用户应该根本不必为此操心。如果你想搞清楚究竟是否需要用到元类，那么你就不需要它。
那些实际用到元类的人都非常清楚地知道他们需要做什么，而且根本不需要解释为什么要用元类。”
 —— Python界的领袖 Tim Peters
'''
