# coding=utf-8
dict1 = {1: 'apple', "two": 'banana', '3': 'orange'}
print(dict1)

# 更新和添加字典元素
dict1[1] = 'pear'         # 更新元素
dict1['four'] = 'ele'     # 添加元素
print(dict1)

# 删除元素和删除字典定义
del dict1[1]              # 删除某个元素
print(dict1)

dict1.clear()             # 删除字典中的所有元素
print(dict1)

del dict1                 # 删除字典的定义

# 字典的key必须不可变,可以用数字、字符串、元组充当,不能用列表
# 字典的value值可以是任意的

# 创建一个新字典,以序列seq中元素做字典的键,val为字典所有键对应的初始值
dict2 = {1: 'guo', 2: 'sheng', 3: 'shi', 4: 'xian'}
dict3 = dict.fromkeys(dict2, '0')
print(dict3)

print(dict2.items())      # 以列表的形式返回字典的(键,值)元组数据

print(dict2.keys())       # 返回一个迭代器,可以使用list()来转换为列表

print(dict2.values())     # 返回一个迭代器,可以使用list()来转换为列表

for i in dict2.keys():
    print(i)              # 返回key值

for i in dict2.values():
    print(i)              # 返回value值

for i, j in dict2.items():
    print(i)              # key值
    print(j)              # value值

for i in dict2.items():
    print(i)              # 返回四个(key,value)元组

for i in dict2:
    print(i)              # 返回key值

# 删除字典给定键key所对应的值,返回值为被删除的值
item = dict2.pop(4)
print(dict2)
print(item)

# 随机返回并删除字典中的一对键和值
item = dict2.popitem()
print(dict2)
print(item)

dict4 = {'book': 21.5, 'cloth': 32, 'glass': '58'}
expensive = max(zip(dict4.values(), dict4.keys()))
print(expensive)
