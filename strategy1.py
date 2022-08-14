# 在strategy中递归算法中添加一个表用来储存中间结果的方法叫做memoization（记忆化/函数值缓存）可以提高递归算法的性能
# 动态规划策略解决的必要条件：问题的最优解包含了更小规模子问题的最优解
# 找零兑换：动态规划解法
# 动态规划算法是采用了一种更有条理的方式来得到问题的解
# 针对找零兑换的动态规划算法 是从 最简单的“1分钱找零”的最优解开始，逐步递加上去，直到我们需要的找零钱数
# 在找零递加的过程中，设法保持每一分钱的递加都是最优解，一直加到求解找零钱数，自然得到的也是最优解
# 递加的过程能保持最优解的关键是，起依赖于更少钱数最优解的简单计算，而更小钱数的最优解已经从strategy中得到过了
def dpMakeChange1(coinValueList,change,minCoins):
    # 从1分开始到change逐个计算最少硬币数
    for cents in range(1,change+1):
        # 1 初始化一个最大值
        coinCount = cents
        # 2 减去每个硬币，向后查最少硬币数，同时记录总的最小数
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        # 3 得到当前最少硬币数，记录在表中
        minCoins[cents] = coinCount
    # 返回最后一个结果
    return minCoins[change]

coinValueList = [1,5,10,21,25]
minCoins = [0] * 64
# print(dpMakeChange1(coinValueList,63,minCoins))
# 找零兑换：动态规划算法扩展
def dpMakeChange(coinValusList,change,minCoins,coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1 #初始化一个新加硬币
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j # 对应最小数量，所减的硬币
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin #记录本步骤加的1个硬币
    return minCoins[change]

def printCoins(coinsUsed,change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

change = 63
coinValueList = [1,5,10,21,25]
coinsUsed = [0] * (change + 1)
coinCount = [0] * (change + 1)

print("Making change for",change,"requires")
print(dpMakeChange(coinValueList,change,coinCount,coinsUsed),"coins")
print("They are:")
printCoins(coinsUsed,change)
print("The used list is as follows:")
print(coinsUsed)