#线性结构——栈：数据排列成线性，后进先出
#用列表list实现栈
class Stack1: #列表首端为栈顶
    def __init__(self):
        self.items = []

    def isEmpty(self):#是空
        return self.items == []

    def push(self,item):#压栈（将item加入栈顶，无返回值）
        self.items.insert(0,item)

    def pop(self):#出栈（将栈顶数据项移除，并返回栈顶的数）
        return self.items.pop(0)

    def peek(self):#“窥视”栈顶数据项，返回栈顶的数据但不会移除数据，栈不被修改
        return self.items[0]

    def size(self):#栈中有多少数据项
        return len(self.items)


class Stack2: #列表尾端为栈顶 (比上面的性能更优)
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


