#coding=utf-8
# 以完全二叉树为例

# 定义节点
class Node(object):
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None

# 定义二叉树
class Tree(object):
    def __init__(self):
        self.root = None
    
    # 使用了队列，将需要后续加入判断的节点放入到了对列右端，从队列左端取数据
    # 程序从根节点开始判断，如果其左右子树为空，直接赋值node，不为空的画，加入队列继续判断
    def add(self, item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        
        queue = [self.root]
        while queue:
          cur_node = queue.pop(0)
          if cur_node.lchild == None:
              cur_node.lchild = node
              return
          else:
              queue.append(cur_node.lchild)
          if cur_node.rchild == None:
              cur_node.rchild = node
              return
          else:
              queue.append(cur_node.rchild)

    # 广度优先遍历    
    # 也是使用了队列的概念，将每一个节点加入到了队列，从队列另一端取数据
    def breadth_travel(self):
        if self.root == None:
            return
        
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=' ')

            if cur_node.lchild != None:
                queue.append(cur_node.lchild)
            if cur_node.rchild != None:
                queue.append(cur_node.rchild)

    # 深度优先遍历
    # 深度优先遍历分为前序遍历、中序遍历、后序遍历
    # 前序遍历：根-左-右
    # 中序遍历：左-根-右
    # 后续遍历：左-右-根
    # 此处使用了递归算法
    def preorder(self, root):
        if root == None:
           return
        print(root.item, end=' ')
        self.preorder(root.lchild)
        self.preorder(root.rchild)
    
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.lchild)
        print(root.item, end=' ')
        self.inorder(root.rchild)
    
    def postorder(self, root):
        if root == None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.item, end=' ')


def main():
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)

    print('广度遍历', end=':')
    tree.breadth_travel()
    print('深度遍历-前序遍历', end=':')
    tree.preorder(tree.root)
    print('深度遍历-中序遍历',end=':')
    tree.inorder(tree.root)
    print('深度遍历-后序遍历',end=':')
    tree.postorder(tree.root)


if __name__ == '__main__':
    main()
