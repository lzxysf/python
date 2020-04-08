# 一个try语句可能包含多个except子句，分别来处理不同的异常，最多会有一个分支会被执行
# 一个excep子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元祖
try:
    a = 1 / 0
except ZeroDivisionError:
    print('ZeroDivisionError')
except RuntimeError:
    print('RuntimeError')
except NameError:
    print('NameError')

try:
    a = 1 / 0
except(ZeroDivisionError, RuntimeError, NameError, TypeError):
    print('error')

try:
    f = open('myfile.txt')
except OSError:
    print('OSError')

# Exception 所有的错误
try:
    a = 1/0
except Exception:
    print('all except')

# try except语句还有一个可选的else子句，如果使用这个子句，必须放在所有的except子句之后
# 这个子句将在try子句没有发生任何异常的时候执行
try:
    a = 2 + 3
    b = open('../others/abc.txt', 'r')
except OSError:
    print('OSError')
else:
    print(b.readline())
# 使用else子句比把所有子句都放在try子句里要好，这样可以避免一些意想不到的，而except没有捕获的异常


# 异常处理并不仅仅处理那些发生在try子句中的异常，而且还能处理子句中的调用函数（甚至间接调用函数）里抛出的异常

# 抛出异常raise
try:
    raise NameError('HiThere')
except Exception as e:
    print(e)


# 自定义异常类
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr('error code:' + str(self.value))


try:
    raise MyError(111)
except MyError as e:
    print(e)

# finally
try:
    a = 1 / 0
except ZeroDivisionError:
    pass
finally:
    print('定义清理行为')
