# 线性结构——队列：特点FIFO(先进先出)，数据项只能从队尾进去，从队首出去，中间不能插入删除数据

class Queue(list):      #用列表实现队列，其中列表尾端作为队列队首
    def __init__(self):
        self.items = []

    def isEmpty(self):          #测试是否空队列，返回值为布尔值
        return self.items == []

    def enqueue(self,item):     #将数据项item添加到队尾，无返回值
        self.items.insert(0,item)

    def dequeue(self):          #从队首移除数据项，返回值为队首数据项，队列被修改
        return self.items.pop()

    def size(self):             #返回队列中数据项的个数
        return len(self.items)



