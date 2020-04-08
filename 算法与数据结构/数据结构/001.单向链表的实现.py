# 定义链表中的节点
class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

# 定义单向链表
class Linkedlist(object):
    def __init__(self):
        self._head = None

    def isEmpty(self):
        if self._head == None:
            return True
        else:
            return False
    
    # 在链表最左端添加元素
    def leftadd(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node
    
    # 在链表最右端添加元素
    def rightadd(self, item):
        node = Node(item)
        cur = self._head
        while cur.next != None:
            cur = cur.next
        cur.next = node

    # 在链表的pos位置插入元素item
    def insert(self, pos, item):
        if pos == 0:
            self.leftadd(item)
            return
        
        node = Node(item)
        cur = self._head
        index = 0
        while index < pos-1:
            cur = cur.next
            index += 1
        node.next = cur.next
        cur.next = node
        
    # 删除链表中值为item的元素
    def remove(self, item):
        cur = self._head
        pre = self._head

        if cur.item == item:
            self._head = cur.next

        while cur != None:
            if cur.item == item:
                pre.next = cur.next
            pre = cur
            cur = cur.next

    # 判断是否有元素item
    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    # 获取元素个数
    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    # 遍历所有元素
    def travel(self):
        cur = self._head
        while cur != None:
          print(cur.item, end=' ')
          cur = cur.next

linklist = Linkedlist()
linklist.leftadd('test1')
linklist.leftadd('test2')
linklist.leftadd('test3')
linklist.rightadd('test4')
linklist.rightadd('test5')
linklist.rightadd('test6')
linklist.insert(3, 'test6')
# print(linklist.isEmpty())
# linklist.travel()
# print('元素个数为', linklist.length())

# linklist.remove('test3')
# linklist.travel()

print('是否拥有元素test6：', linklist.search('test6'))
