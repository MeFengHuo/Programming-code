# 二叉树用链表实现
class BinaryTree:
    def __init__(self,rootObj):     #二叉树节点
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):   #插入左子树
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):  #插入右子树
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):    #取得右子树
        return self.rightChild

    def getLeftChild(self):     #取得左子树
        return  self.leftChild

    def setRootVal(self,obj):   #设置根值
        self.key = obj

    def getRootVal(self):       #取得根值
        return self.key


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())
r.getLeftChild().insertRight('d')