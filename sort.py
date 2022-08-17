# 排序

def bubbleSort(alist):  #冒泡排序
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,31,44,55,20]
bubbleSort(alist)
print(alist)

def shortBubbleSort(alist):     #冒泡排序：性能改进
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1

blist = [20,30,40,13,45,50,60,80,74,100,]
shortBubbleSort(blist)
print(blist)

def selectionSort(alist):   #选择排序
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

clist = [5,1,4,6,7,41,20,9,5]
selectionSort(clist)
print(clist)

