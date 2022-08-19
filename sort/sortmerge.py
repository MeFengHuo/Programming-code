# 归并排序：典型使用分治策略案例
def mergeSort(alist):
    print("Splitting",alist)
    if len(alist) > 1:          #递归基本结束条件
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)     #递归调用自身
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i<len(lefthalf) and j<len(righthalf):
            # 拉链式交错把左右半部从小到大归并到结果列表中
            if lefthalf[i]<righthalf[i]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i<len(lefthalf):
            # 归并左半部剩余项
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j<len(righthalf):
            # 归并右半部剩余项
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

    print("Merging",alist)
alist = [5,-4,6,18,13,45,15,33,-9,0,]
mergeSort(alist)
print(alist)

def merge_sort(lst):    #更python版
    # 递归结束条件
    if len(lst) <= 1:
        return lst

    # 分解问题，并递归调用
    middle = len(lst) // 2
    lefthalf = merge_sort(lst[:middle])
    righthalf = merge_sort(lst[middle:])

    # 合并左右半部，完成排序
    merged = []
    while lefthalf and righthalf:
        if lefthalf[0] <= righthalf[0]:
            merged.append(lefthalf[0])
        else:
            merged.append(righthalf[0])

    merged.extend(righthalf if righthalf else lefthalf)
    return merged

# lst = [5,-4,6,18,13,45,15,33,-9,0,]
# merge_sort(lst)
# print(lst)
