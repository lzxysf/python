'''
scope即命名空间
'''
print(globals()) # 当前全局变量的字典表示
print(locals())  # 当前局部变量的字典表示

'''
python使用LEGB的顺序来查找一个符号对应的对象
locals----enclosing function----globals----builtins

locals--当前所在的命名空间
enclosing function--外部嵌套函数的命名空间
globals--全局变量
builtins--内建模块的命名空间

Python 在启动的时候会自动为我们载入很多内建的函数、类，
比如 dict，list，type，print，这些都位于 __builtin__ 模块中
'''
