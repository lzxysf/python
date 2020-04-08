# 定义链表中的节点
class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

# 定义单向循环链表
class SinCycLinkedlist(object):
    def __init__(self):
        self._head = None
    
    def is_empty(self):
        return self._head == None
    
    def length(self):
        if self.is_empty():
            return 0
        
        count = 1
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count
    
    def travel(self):
        if self.is_empty():
            return
        cur = self._head
        while cur.next != self._head:
            print(cur.item)
            cur = cur.next
        print(cur.item)

    def leftadd(self, item):
        node = Node(item)
        if self.is_empty():
            node.next = node
            self._head = node
        else:
            node.next = self._head
            # 定位到最后一个节点，将最后一个节点指向新的第一个节点node
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            self._head = node
            cur.next = self._head

    def rightadd(self, item):
        node = Node(item)
        if self.is_empty():
            node.next = node
            self._head = node
        else:
            node.next = self._head
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos == 0:
            self.leftadd(item)
            return
        node = Node(item)
        cur = self._head
        count = 0
        while count < pos - 1:
            cur = cur.next
            count += 1
        # 如果要插入的是最后一个位置
        if cur.next == self._head:
            self.rightadd(item)
        # 如果要插入的不是最后一个位置
        else:
            node.next = cur.next
            cur.next = node

    def search(self, item):
        cur = self._head
        if self.is_empty():
            return False
        while cur.next != self._head:
            if cur.item == item:
                return True
            cur = cur.next
        if cur.item == item:
            return True
        return False

    def remove(self, item):
        if self.is_empty():
            return
        cur = self._head
        # 要删除的是第一个节点的话
        if cur.item == item:
            # 链表不只有一个节点的话
            if cur.next != self._head:
              while cur.next != self._head:
                cur = cur.next
              self._head = self._head.next
              cur.next = self._head
            # 链表只有一个节点
            else:
                self.head = None
            return

        # 要删除的是中间的节点的话
        cur = self._head
        pre = self._head
        while cur.next != self._head:
            if cur.item == item:
                pre.next = cur.next
                return
            pre = cur
            cur = pre.next
        
        # 要删除的是最后一个节点的话
        if cur.item == item:
            pre.next = self._head


if __name__ == "__main__":
    linklist = SinCycLinkedlist()
    linklist.leftadd('test1')
    linklist.leftadd('test2')
    linklist.rightadd('test3')
    linklist.rightadd('test3')
    linklist.rightadd('test4')

    linklist.travel()
    print('长度:', linklist.length())
    print('是否为空:', linklist.is_empty())
    print('是否找到test4:', linklist.search('test4'))
    
    linklist.remove('test4')
    linklist.travel()
    print('是否找到test4:', linklist.search('test4'))

    linklist.insert(1, 'test5')
    linklist.insert(0, 'test6')
    linklist.insert(6, 'test7')
    linklist.travel()
