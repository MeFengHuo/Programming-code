# 树逻辑：二叉堆(用列表实现)

class BinHeap:
    def __init__(self):         #创建一个空二叉堆对象
        self.heaplist = [0]
        self.currentSize = 0

    def percUp(self,i):         #沿堆顺序(树路径:从叶节点到根)上浮
        while i//2 > 0:
            if self.heaplist[i] < self.heaplist[i//2]:
                tmp = self.heaplist[i//2]               # 当前子节点与父节点交换上浮
                self.heaplist[i//2] = self.heaplist[i]
                self.heaplist = tmp
            i = i // 2

    def insert(self,k):         #将新key加入到堆中
        self.heaplist.append(k) #新key添加到列表队尾[逻辑树中的叶节点]
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)   #新key上浮

    def percDown(self,i):       #沿堆顺序(树路径:从根到叶节点)下沉
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                tmp = self.heaplist[i]                  #父节点与子节点交换下沉
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc

    def minChild(self,i):       #取子节点最小值
        if i * 2 + 1 > self.currentSize:    #唯一子节点
            return i * 2
        else:
            if self.heaplist[i*2] < self.heaplist[i*2+1]:   #左右节点比较，返回最小值
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):           #返回堆中的最小项，同时从堆中删除
        retval = self.heaplist[1]           #移走堆顶[堆列表中的第二项，第一项为0未使用]
        self.heaplist[1] = self.heaplist[self.currentSize]  #将列表最后一项放到逻辑堆顶
        self.currentSize = self.currentSize - 1
        self.heaplist.pop()         #移除列表最后一项（因为已经放到堆顶，重复项不需要）
        self.percDown(1)            #新堆顶下沉
        return retval

    def buildHeap(self,alist):  #创建新堆，从无序表生成“堆”
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heaplist = [0] + alist[:]
        print(len(self.heaplist),i)
        while i>0:
            print(self.heaplist,i)
            self.percDown(i)
            i = i - 1
        print(self.heaplist,i)

bh = BinHeap()
bh.buildHeap([5,1,40,2,4,20,8,9,])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())