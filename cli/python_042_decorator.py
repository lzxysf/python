# 装饰器
# 写代码要遵循开放封闭的原则，即已经完成的功能代码不允许被修改，但可以被扩展

# 装饰器的功能
# 1.引入日志
# 2.函数执行时间统计
# 3.函数执行前预备处理
# 4.函数执行后清理功能
# 5.权限校验等场景
# 6.缓存


def logging(fun):  # 定义装饰器函数

    def wrapped():  # 在原方法前后加入进出方法的日志
        print("[DEBUG] ENTER {}".format(fun.__name__))
        fun()
        print("[DEBUG] EXIT {}".format(fun.__name__))

    return wrapped


@logging          # 使用装饰器，此处代码相当于test = logging(test) ; test()
def test():
    print("test function")


test()


# 被装饰的函数有参数
# 还是上面的例子，修改如下
print('-'*30)


def logging(fun):

    def wrapped(data):
        print("[DEBUG] ENTER {}".format(fun.__name__))
        fun(data)
        print("[DEBUG] EXIT {}".format(fun.__name__))

    return wrapped


@logging
def test(data):
    print(data)


test('hello')


# 被装饰的函数有不定长参数
# 还是上面的例子，修改如下
print('-'*30)


def logging(fun):

    def wrapped(*args, **kwargs):
        print("[DEBUG] ENTER {}".format(fun.__name__))
        fun(*args, **kwargs)
        print("[DEBUG] EXIT {}".format(fun.__name__))

    return wrapped


@logging
def test(a, b, c):
    value = a + b + c
    print(value)


test(1, 5, 8)


# 在原有装饰器的基础上，设置外部变量
# 还是上面的例子，修改如下
print('-'*30)


def logging(level):
    def log(fun):
        def wrapped(*args, **kwargs):
            print("[{}] ENTER {}".format(level, fun.__name__))
            fun(*args, **kwargs)
            print("[{}] EXIT {}".format(level, fun.__name__))
        return wrapped
    return log


@logging(level='INFO')
def test(a, b, c):
    value = a + b + c
    print(value)


test(1, 5, 8)