# 谢尔排序：在插入排序insertionsort的基础上，对无序表进行“间隔”划分子列表，每个子列表都执行插入排序
def shellsort(alist):
    sublistcount = len(alist) // 2  #间隔设定
    while sublistcount > 0:

        for startposition in range(sublistcount):   #子列表排序
            gapInsertionSort(alist,startposition,sublistcount)

        print("After increments of size",sublistcount,"The list ia",alist)

        sublistcount = sublistcount // 2    #间隔缩小

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue

alist = [5,0,20,-4,7,60,13,12,17,52,45,]
shellsort(alist)
print(alist)
