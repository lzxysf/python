# 闭包
# 在外层函数内定义了一个内层函数，且内层函数使用了外层函数的变量，并且外层函数将内层函数作为一个返回值返回，这就是闭包的概念

# 闭包优化了变量，原来需要类完成的工作，闭包也可以完成
# 闭包引用了外部函数的局部变量，外部函数的局部变量没有及时释放，消耗内存


def cal(a, b):
    def wrapped(x):
        value = a * x + b
        return value

    return wrapped


foo1 = cal(1, 1)
print(foo1(5))

foo2 = cal(2, 3)
print(foo2(5))
