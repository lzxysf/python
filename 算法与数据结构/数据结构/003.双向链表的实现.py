# 定义链表中的节点
class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


# 定义双向链表
class DoLinkedlist(object):
    def __init__(self):
        self._head = None
    
    def is_empty(self):
        return self._head == None
    
    def length(self):
        if self.is_empty():
            return 0
        cur = self._head
        count = 1
        while cur.next != None:
            count += 1
            cur = cur.next
    
    def travel(self):
        if self.is_empty():
          return
        cur = self._head
        while cur.next != None:
            print(cur.item, end=' ')
            cur = cur.next
        print(cur.item)
    
    def leftadd(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            return
        node.next = self._head
        self._head.prev = node
        self._head = node
    
    def rightadd(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            return
        cur = self._head
        while cur.next != None:
            cur = cur.next
        node.prev = cur
        cur.next = node
    
    def insert(self, pos, item):
        if self.is_empty():
            self.leftadd(item)
            return
        # 插入最前端节点
        if pos == 0:
            self.leftadd(item)
            return
        cur = self._head
        count = 0
        while count < pos - 1:
            cur = cur.next
            count += 1
        # 插入最后端节点
        if cur.next == None:
            self.rightadd(item)
        # 插入中间的节点
        else:
            node = Node(item)
            node.next = cur.next
            cur.next.prev = node
            node.prev = cur
            cur.next = node

    def search(self, item):
        if self.is_empty():
            return False
        cur = self._head
        while cur.next != None:
            if cur.item == item:
                return True
            cur = cur.next
        if cur.item == item:
            return True
        return False

    def remove(self, item):
        if self.is_empty():
            return
        # 要删除的是第一个节点
        if self._head.item == item:
            # 只有这一个节点
            if self._head.next == None:
                self._head = None
            # 不止有一个节点
            else:
                self._head.next.prev = None
                self._head = self._head.next
            return
        # 要删除的是中间的节点
        cur = self._head
        while cur.next != None:
            if cur.item == item:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return
            cur = cur.next
        # 要删除的是最后一个节点
        if cur.item == item:
            cur.prev.next = None

if __name__ == '__main__':
    linklist = DoLinkedlist()
    linklist.rightadd('test2')
    linklist.rightadd('test3')
    linklist.leftadd('test1')
    linklist.insert(1, 'test4')
    linklist.leftadd('test1')
    linklist.travel()

    print('是否存在：', linklist.search('test4'))

    linklist.remove('test1')
    linklist.travel()
