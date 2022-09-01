# 树遍历和应用
def preOrder(tree):     #递归遍历树：前序遍历（根，左子树，右子树）
    if tree:
        print(tree.getRootVal())
        preOrder(tree.getLeftChild())
        preOrder(tree.getRightChild())

def postOrder(tree):    #递归遍历树：后序遍历（左子树，右子树，根）
    if tree != None:
        postOrder(tree.getLeftChild())
        postOrder(tree.getRightChild())
        print(tree.getRootVal())

def inOrder(tree):      #递归遍历树：中序遍历（左子树，根，右子树）
    if tree != None:
        inOrder(tree.getLeftChild())
        print(tree.getRootVal())
        inOrder(tree.getRightChild())

from binarytreenoderef import BinaryTree
import operator

x = BinaryTree('*')
x.insertLeft('+')
l = x.getLeftChild()
l.insertLeft(4)
l.insertRight(5)
x.insertRight(7)

def printexp(tree):     #用中序遍历树并以全括号的形式把树输出成字符串
    sVal = ""
    if tree:
        sVal = "(" + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ")"
    return sVal

def postOrdereval(tree):    #用递归算出中序表达式解析树的值
    opers = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postOrdereval(tree.getLeftChild())
        res2 = postOrdereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()

print(printexp(x))
print(postOrdereval(x))