# 插入排序：就像整理扑克牌顺序
def insertionSort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]     #新项/插入项
        position = index

        while position>0 and alist[position-1]>currentvalue:    #对比，移动
            alist[position] = alist[position-1]
            position = position - 1

        alist[position] = currentvalue  #插入新项

alist = [1,5,4,10,24,16,11,55,22]
insertionSort(alist)
print(alist)