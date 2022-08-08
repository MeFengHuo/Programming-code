#线性结构之无序表：数据项排列位置与数据项的相对位置有关的数据集

class Node:                     #定义链表的节点(包含两个属性，内容与指向)
    def __init__(self,initdata):
        self.data = initdata    #节点中的数据内容
        self.next = None        #节点指向下一个节点，当指向为空时节点为空

    def getData(self):          #方法：获取节点数据
        return self.data

    def getNext(self):          #方法：获取下一个节点
        return self.next

    def setData(self,newdata):  #方法：修改数据
        self.data = newdata

    def setNext(self,newnext):  #方法：修改节点的下一个指向引用
        self.next = newnext

# temp = Node(22)
# print(temp.getData())

class UnorderedList:            #用链表实现无序表
    def __init__(self):         #定义表头
        self.head = None

    def isEepty(self):          #无序表是否为空
        return self.head == None

    def add(self,item):         #无序表中添加数据项，假设数据项不在无序表中
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):           #无序表长度
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):       #无序表中查找item，返回布尔值
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return  found

    def remove(self,item):      #从无序表中移除item，无序表被修改，item原先应存放在表中
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.length())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.length())

mylist.remove(54)
print(mylist.length())
mylist.remove(93)
print(mylist.length())
mylist.remove(31)
print(mylist.length())
print(mylist.search(93))