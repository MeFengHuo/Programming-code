#用栈实现小括号（）左右对称匹配
from Stack import Stack

def parCherker(symbolString):
    s = Stack()
    balanced = True #用于是否匹配
    index = 0 #用于索引
    while index < len(symbolString) and balanced:
        symbol = symbolString[index] #取出参数第n个元素
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index +1

    if balanced and s.isEmpty():
        return True
    else:
        return False

# print(parCherker('((()))'))
# print(parCherker('(()())'))

def parChecker_all(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False
        index = index +1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print(parChecker_all("{{([][])}()}"))
print(parChecker_all('[{()}'))