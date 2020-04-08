class Stack(object):
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    # 返回栈顶元素
    def peek(self):
        return self.items[self.size()-1]

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print('栈大小:', s.size())
    print(s.pop())
    print(s.peek())
    print('是否为空:', s.is_empty())
