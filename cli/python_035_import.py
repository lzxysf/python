# coding=utf-8
import sys
print(sys.path)

'''
['/home/coding/workspace/cli', 
'/usr/lib/python35.zip', 
'/usr/lib/python3.5', 
'/usr/lib/python3.5/plat-x86_64-linux-gnu',
'/usr/lib/python3.5/lib-dynload',
'/usr/local/lib/python3.5/dist-packages',
 '/usr/lib/python3/dist-packages']

路径搜索，从上面的目录中依次查找要导入的模块文件

添加模块路径
sys.path.append()
sys.path.insert()
'''

'''
重新导入模块
模块被导入后改变了，如果此时想重新导入，不能再用import导入
import module
from imp import *
reload(module)
'''
import os
from imp import *
reload(os)

'''
循环导入
如果在a中导入了b，在b中导入了a，这就是循环导入了
这种情况是禁止的
需要通过顶层设计避免这种情况的出现，比如抽象出公共的c，在c中同时调用a和b
'''
