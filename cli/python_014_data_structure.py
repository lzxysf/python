# coding=utf-8
# 堆栈是一个后进先出的数据结构
# 把列表当作堆栈使用，使用列表的append方法在堆栈顶插入元素，使用列表的pop方法在堆栈顶删除元素
import collections

stack = [3, 4, 5]
stack.append(9)
stack.append(10)
print(stack)
stack.pop()
print(stack)

# 队列是一个先进先出的数据结构
# 不可直接把列表当作队列使用，因为列表操作末尾数据进行添加删除比较容易，但
# 操作开头的数据进行添加和删除需要将列表中的元素一个个移动位置，因此效率是很低的
queue = collections.deque(['Eric', 'Deril', 'Mical'])
queue.append('Deney')
queue.append('Steven')
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)


# 列表推导式
vec = [2, 4, 6]
vec1 = [(i, i**2) for i in vec]
print(vec1)

print(queue.popleft())
print(queue)


# 列表推导式
vec = [2, 4, 6]
vec1 = [(i, i**2) for i in vec]
print(vec1)

vec2 = [3 * i for i in vec if i >= 4]
print(vec2)

# 在序列中遍历，索引位置和对应值可以用enumerate函数同时得到
vec3 = ['juice', 'water', 'tea']
for i, v in enumerate(vec):
    print(i, end=' ')
    print(v)

# 同时遍历两个或更多序列，可以用zip()组合
questions = ['favaorite color', 'your name', 'your email']
answers = ['yellow', 'lsf', '126.com']
for i, v in zip(questions, answers):
    print('what is {0}? it is {1}'.format(i, v))

# 反向遍历
for i in reversed(range(1, 10, 2)):
    print(i)

print('*'*20)

# 顺序遍历
basket = ['apple', 'orange', 'banana', 'melon', 'apple', 'juice']
for i in sorted(set(basket)):
    print(i)
