# 递归实现， 递归调用三特点：
# 1递归算法必须有一个基本结束条件（最小规模问题的直接解决）
# 2递归算法必须能改变状态向基本结束条件演进（减小问题规模）
# 3递归算法必须调用自身（解决减小了规模的相同问题）
def toStr(n, base):  # 递归实现进制转换
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]  # 最小规模
    else:
        return toStr(n // base, base) + convertString[n % base]  # 减小规模，调用自身


print(toStr(1234, 16))


def listsum(numList):  # 递归实现数列求和
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])


print(listsum([1, 3, 5, 7, 9, 11, 13, 15]))
