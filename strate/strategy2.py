# 动态规划策略与贪心策略的区别
# 贪心策略算法要求“局部最优等同于总体最优”
# 动态规划算法要求“问题最优解包括规模更小相同问题的最优解”
# 贪心算法能解的问题，动态规划一定也能解；相反，动态规划能解的问题贪心算法未必能解
# 动态规划适用范围：
#   1 最优 子结构（问题的最优解包含子问题的最优解）
#   2 无后效性（当前阶段的状态仅由以前阶段决定，后续阶段状态的变化不会影响当前阶段的状态）
#   3 重复子问题（解决问题过程中的子问题存在大量重叠（冗余计算））
# 博物馆大盗问题
# 动态规划解法
# 宝物的重量和价值
tr = [None,{"w":2,"v":3},{"w":3,"v":4},{"w":4,"v":8},{"w":5,"v":8},
            {"w":9,"v":10}]

# 大盗最大承重
max_w = 20

# 初始化二维表格m[（i,w）]
# 表示前i个宝物中，最大重量w的组合，所得到的最大价值
# 当i什么都不取，或w上限为0，价值均为0
m = {(i,w):0 for i in range(len(tr))
                for w in range(max_w+1)}
# print(m)
# 逐个填写二维表格
for i in range(1,len(tr)):
    for w in range(1,max_w+1):
        if tr[i]["w"] > w:  #装不下第i个宝物
            m[(i,w)] = m[(i-1,w)]   #不装第i个宝物
        else:
            # 不装第i个宝物，装第i个宝物，两种情况下最大价值
            m[(i,w)] = max(
                m[(i,w)],m[(i-1,w-tr[i]["w"])]+tr[i]["v"]
            )
#输出结果
# print(m)
# print(m[(len(tr)-1,max_w)])

# 递归解法
# 宝物的重量和价值
tr = {(2,3),(3,4),(4,8),(5,8),(9,10)}
# 大盗最大承重
max_w = 20
# 初始化记忆性表格m
# key是(宝物组合，最大重量)，value是最大价值
m = {}

def thief(tr,w):
    if tr == set() or w == 0:
        m[(tuple(tr),w)] = 0   #tuple 是key的要求
        return 0
    elif (tuple(tr),w) in m:
        return m[(tuple(tr),w)]
    else:
        vmax = 0
        for t in tr:
            if t[0] <= w:
                #逐个从集合中去掉某个宝物，递归调用
                #选出所有价值中的最大值
                v = thief(tr-{t},w-t[0]) + t[1]
                vmax = max(vmax,v)
        m[(tuple(tr),w)] = vmax
        return vmax

print(thief(tr,max_w))
