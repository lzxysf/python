# coding=utf-8
# 集合(set)是一个无序的不重复元素序列
# 可以使用大括号{}或set()来创建

# 定义的集合中有重复元素时,集合会自动去重
set1 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(set1)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)

# 集合运算
print(a-b)              # a中有而b中没有的元素集合
print(a | b)            # a和b中所有的元素集合
print(a & b)            # a和b中共有的元素集合
print(a ^ b)            # 不同时包含于a和b中的元素集合

set2 = set(("Google", "baidu", "tencent"))
set2.add('sogou')                                 # 增加
print(set2)
set2.remove('sogou')                              # 删除
print(set2)
set2.discard('baidu')                             # 删除,且如果元素不存在不会发生错误
print(set2)

print(set2.pop())                                 # 删除一个元素并返回集合被删除的这个元素
print(set2)

print(len(set2))                                  # 计算集合的个数
set2.clear()                                      # 清空集合
print(set2)
