# coding=utf-8
tup1 = ()              # 创建空元组
tup1 = (5,)           # 当元组中只有一个元素时,要加逗号,否则会认为是这个元素的类型而不是元组
print(tup1)

# 元组中元素是不允许修改的,即tup1[0] = 1这样是不允许的,但是可以对tup1重新赋值或连接其它元组
tup1 = (1, 12)
print(tup1)

# 元组中元素是不允许删除的,但是可以将整个元组的定义删除,如
del tup1

# 计算元组中元素数量,使用len
tup2 = (5, 8, 'ten')
print(len(tup2))

# python中任意无符号的对象,以逗号隔开,默认都是元组
tup3 = 1, 'apple', 4+8j, 'xyz'
print(tup3)

# tuple(seq) 将列表转换为元组
list1 = [1, 2, 'xyz', 'abc']
tup4 = tuple(list1)
print(tup4)

# 元组的各个元素不可变, 但是当元组的某个元素为列表时, 这个列表是可变的, 因为元组中存储的是列表的地址而不是列表本身
tup5 = ('java', 'python', list1)
print(tup5)
tup5[2].remove('xyz')
print(tup5)
