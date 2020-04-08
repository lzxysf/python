# coding=utf-8

arr = []
arr.append('google')              # 在列表末尾添加新的对象
arr.append('python')
arr.append('java')
print(arr)
print(arr.count('java'))          # 统计列表中某个元素的数量

print(arr.index('java'))          # 从列表中找出某个值第一个匹配项的索引位置

arr.insert(1, 'C')                 # 在原来的列表位置1处插入元素‘C’

print(arr)

del arr[1]
print(arr)
print(len(arr))

while len(arr)>0:
    x = arr.pop(0)                 # 移除列表中的一个元素，并且返回该元素的一个值，默认返回最后一个，但是也可以在pop中用参数指定
    print(x)

arr = ['apple', 'melon', 'orangle']
arr.remove('melon')               # 移除列表中某个值的第一个匹配项，区别于del，del是移除确定位置的项
print(arr)

arr.append('aoe')
arr.reverse()                     # 列表反转
print(arr)

arr.sort()
print(arr)

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a*3)
print(3 in a)
print(max(a))
print(min(a))

# list()作用是将元组或字符串转换成列表
c = ('a', 'b', 'c', 'd', 'e')
print(c)
d = list(c)
print(d)

e = "hello world"
f = list(e)
print(e)
print(f)


