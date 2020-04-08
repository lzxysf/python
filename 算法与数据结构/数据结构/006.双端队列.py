'''
Deque() 创建一个空的双端队列
add_front(item) 从队头加入一个item元素
add_rear(item) 从队尾加入一个item元素
remove_front() 从队头删除一个item元素
remove_rear() 从队尾删除一个item元素
is_empty() 判断双端队列是否为空
size() 返回队列的大小
'''
class Deque(object):
    def __init__(self):
        self.items = []
    
    def add_front(self, item):
        self.items.insert(0, item)
    
    def add_rear(self, item):
        self.items.append(item)
    
    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

if __name__ == '__main__':
    q = Deque()
    q.add_front(1)
    q.add_front(2)
    q.add_rear(1)
    q.remove_front()
    q.remove_rear()
    print('是否为空:', q.is_empty())
    print('队列大小:', q.size())
