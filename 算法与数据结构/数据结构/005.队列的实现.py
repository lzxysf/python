class Queue(object):
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    print('队列的长度', q.size())
    print('是否为空', q.is_empty())
    