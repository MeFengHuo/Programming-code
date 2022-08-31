# 树结构应用：用二叉树解析全括号表达式

from Stack import Stack    #栈
from binarytreenoderef import BinaryTree #链表二叉树

def buildParseTree(fpexp):          #将中继表达式转换成二叉树结构
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)      #入栈下降
    currentTree = eTree     #当前树节点
    for i in fplist:
        if i == "(":                    #表达式开始
            currentTree.insertLeft('')
            pStack.push(currentTree)    #当前树节点入栈下降
            currentTree = currentTree.getLeftChild()
        elif i not in ['+','-','*','/',')']:    #操作数
            currentTree.setRootVal(int(i))
            parent = pStack.pop()           #当前树节点出栈上升
            currentTree = parent
        elif i in ['+','-','*','/']:        #操作符
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ")":                      #表达式结束
            currentTree = pStack.pop()      #当前节点出栈上升
        else:
            raise ValueError
    return eTree
# 中继表达式解析树求值
import operator
def evaluate(tree):     #递归表达式解析树求值
    opers = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}

    leftC = tree.getLeftChild()         #缩小规模
    rightC = tree.getRightChild()

    if leftC and rightC:
        fn = opers[tree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))     #递归调用
    else:
        return tree.getRootVal()    #基本结束条件



pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print(evaluate(pt))