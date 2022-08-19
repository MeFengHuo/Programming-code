# 栈应用:数学中继表达式转换成后继表达式

from Stack import Stack #导入栈类

def infixToPostfix(infixexpr):
    prec = {} #用字典定义操作符优先级
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack() #准备栈
    postfixList = [] #准备列表
    tokenlist = infixexpr.split() #将参数表达式切片成单个字符

    for token in tokenlist: #遍历参数表达式
        if token in "ABCDEFGHIJKLMNOPRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)   #将操作数加入到列表
        elif token == "(":              #如果参数表达式元素是（将其压入栈
            opStack.push(token)
        elif token == ")":              #如果参数表达式元素是）则将已经压入栈的元素出栈
            topToken = opStack.pop()
            while topToken != "(":      #判断出栈的元素不是（则将出栈的元素添加到列表，继续出栈元素直到是（
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):    #peek()函数：窥视栈顶但不出栈
                #  当（栈不空）且（（栈顶操作符元素在字典中的值）大于等于（遍历参数表达式中操作符元素在字典值））
                postfixList.append(opStack.pop())   #栈顶元素出栈并加入到列表
            opStack.push(token) #将参数表达式元素压入栈

    while not opStack.isEmpty(): #当栈不空，将栈顶元素出栈加入到列表
        postfixList.append(opStack.pop())
    return  " ".join(postfixList) #将列表里的元素合并成字符串作为返回值

# print(infixToPostfix("A * B + C * C"))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

def postfixEval(postfixExpr):   #后继表达式做数值运算，其中规定实参中每个元素用空格符隔开
    operandStack = Stack()
    tokenList = postfixExpr.split()
    alist = [str(i) for  i in range(100)]   #alist列表限定了实参表达式中操作数元素的取值范围（0-100）

    for token in tokenList:
        if token in alist:
            operandStack.push(int(int(token)))  #将实参元素转换成整数压入栈
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)    #用函数doMath做数值运算
            operandStack.push(result)   #运算结果压入栈
    return operandStack.pop()       #以出栈结果作为返回值

def doMath(op,op1,op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('70 80 + 30 20 + /'))



