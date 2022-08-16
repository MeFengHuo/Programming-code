# 顺序查找
def sequentialSearchi(alist,item):  #无序表顺序查找
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

testlista = [1,2,32,8,17,19,42,13,0]
print(sequentialSearchi(testlista,3))
print(sequentialSearchi(testlista,13))

def orderedSequentialSearch(alist,item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found

testlistb = [0,1,2,8,13,17,19,32,42,]
print(orderedSequentialSearch(testlistb,3))
print(orderedSequentialSearch(testlistb,13))

def binarySearch(alist,item):   #顺序表的二分查找
    first = 0
    last = len(alist) - 1
    found = False

    while first<=last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

testlistb = [0,1,2,8,13,17,19,32,42,]
print(binarySearch(testlistb,3))
print(binarySearch(testlistb,13))

def binarySearch_1(alist,item):     #二分查找递归算法
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)

testlistb = [0,1,2,8,13,17,19,32,42,]
print(binarySearch_1(testlistb,3))
print(binarySearch_1(testlistb,13))
