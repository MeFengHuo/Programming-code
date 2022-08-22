# 树结构：树是由节点node和边side组成，每个树都有一个根节点root和零个或多个子节点组成；边side的个数一般决定了一个树结构的分叉树；
# 比如：两个边的树结构成为二叉树，三个是三叉树；同时又把根节点称为父节点，根节点直接通过边side连接的节点称为子节点；
# 父亲节点和直接相连的子节点，可以分为两层，一层是父亲节点，另一层是子节点；如果把父亲节点视为0层，那么子节点就是1层，高度是1；一个树结构可以由多层组成

# binarytreelist 用列表实现的二叉树
def Binarytree(r):      #创建一个新的二叉树
    return [r,[],[]]    #列表构造一个树节点，其中根r，左叉树[],右叉树[]

def insertLeft(root,newBranch):     #将新节点插入树中作为其直接左节点
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def insertRight(root,newBranch):    #将新节点插入树中作为其直接右节点
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):               #取得根节点
    return root(0)

def setRootVal(root,newval):        #设置根节点
    root[0] = newval

def getLeftChild(root):             #取得左节点
    return root[1]

def getRightChild(root):            #取得有节点
    return root[2]

r = Binarytree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
k = getRightChild(r)
print(l,k,sep="\n")
setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))