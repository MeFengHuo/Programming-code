#线性结构之双端队列 首尾两端都可以加入移除数据项

class Deque:    #用列表实现双端队列，列表0项位双端队列的尾部，-1项为双端队列的首部
    def __init__(self):         #创建一个空的双端队列
        self.items = []

    def isEmpty(self):          #返回deque是否为空
        return self.items == []

    def addFront(self,item):    #将item加入到队首
        self.items.append(item)

    def addRear(self,item):     #将item加入到队尾
        self.items.insert(0,item)

    def removeFront(self):      #从队首移除数据项，返回值为移除的数据项
        return self.items.pop()

    def removeRear(self):       #从队尾移除数据项，返回值为移除的数据项
        return self.items.pop(0)

    def size(self):             #返回deque中包含数据项的个数
        return len(self.items)

