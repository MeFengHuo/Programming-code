# 树逻辑应用：二叉查找树
class TreeNode:         #对象：二叉查找树的树节点
    def __init__(self,key,val,left=None,right=None,parent=None):    #节点初始化
        self.key = key              #键值
        self.payload = val          #数据项
        self.leftChild = left       #左子节点
        self.rightChild = right     #右子节点
        self.parent = parent        #父节点

    def hasLeftChild(self):         #方法：当前节点是否有左节点
        return self.leftChild

    def hasRightChild(self):        #方法：当前节点是否有右节点
        return self.rightChild

    def isLeftChild(self):          #方法：判断当前节点是否是父亲节点的左节点
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):         #方法：判断当前节点是不是父亲节点的右节点
        return self.parent and self.parent.rightChild == self

    def isRoot(self):               #方法：判断当前节点是不是根节点
        return not self.parent

    def isLeaf(self):               #方法：判断当前节点是不是叶节点
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):       #方法：判断当前节点是不是有其他任一个节点
        return self.leftChild or self.rightChild

    def hasBothChildren(self):      #方法：判断当前节点是不是同时有两个节点
        return  self.leftChild and self.rightChild

    def replaceNodeData(self,key,value,lc,rc):  #方法：更换当前节点
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySerchTree:          #二叉查找树对象
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    # def __iter__(self):           #特殊方法：迭代器
    #     return self.root.__iter__()
    def __iter__(self):             #特殊方法：迭代器
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def put(self,key,val):      #方法：插入key构造二叉查找树（BST）
        #首先看BST是否为空，如果一个节点都没有，那么key成为根节点root；否则，就调用一个递归函数_put(key,val,root)来放置key
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):     #方法：_put辅助方法
        '''如果key比currentNode小，那么_put到左子树
                但如果没有左子树，那么key就成为左子节点
            如果key比currentNode大，那么_put到右子树
                但如果没有右子树，没有key就成为右子节点'''
        if key < currentNode.key:
            if currentNode.hasLeftChild():  #递归左子树
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild(): #递归右子树
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self, key, value):      #特殊方法：索引赋值
        self.put(key,value)

    def get(self,key):              #获取二叉查找树key的数据项
        #和put，_put方法原理类似
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self,key,currentNode): # get方法的递归辅助方法
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key > key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self, key):     #特殊方法：索引取值>>实现 val = myZipTree['PKU']
        return self.get(key)

    def __contains__(self, key):   #特殊方法：in归属判断操作>>实现’PKU‘ in myZipTree的归属判断
        if self._get(key,self.root):
            return True
        else:
            return False

    def delete(self,key):           #方法：删除键值为key的节点
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)   #remove方法具体实现在下面
                self.size = self.size - 1
            else:
                raise KeyError('Error,key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error,key not in tree')

    def __delitem__(self, key):     #特殊方法：删除>>实现：del myZipTree['PKU']这样的删除操作语句
        self.delete(key)



    def remove(self, currentNode):
        if currentNode.isLeaf():    #如果删除的当前节点是叶节点
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():     #如果删除的当前节点有两个子节点
            succ = currentNode.findSuccessor()  #方法findSuccessor()
            succ.spliceOut()                    #方法spleceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:                       #如果当前节点只有一个子节点
            if currentNode.hasLeftChild():      #如果当前节点拥有的唯一子节点是左子节点
                if currentNode.isLeftChild():       #左子节点删除
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():    #右子节点删除
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:                               #根节点删除
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:                               #如果当前节点拥有的唯一子节点是右子节点
                if currentNode.isLeftChild():       #左子节点删除
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():    #右子节点删除
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:                               #根节点删除
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)

    def findSuccessor(self):        #方法：寻找当前节点的后继节点
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):        #方法：摘除节点
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

mytree = BinarySerchTree()
mytree[3] = 'red'
mytree[4] = 'blue'
mytree[6] = 'yellow'
mytree[2] = 'at'

print(3 in mytree)
print(mytree[6])
del mytree[2]
print(mytree[2])