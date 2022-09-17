# 图应用：骑士周游问题->深度优先算法
from graph import Graph,Vertex

def genLegalMoves(x,y,bdSize):      #将军棋子合法移动
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),   #棋子相对移动方位
                   ( 1, -2), ( 1, 2), ( 2, -1), ( 2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            newMoves.append((newY,newY))
    return newMoves

def legalCoord(x, bdSize):          #将军棋子移动边界判断：确认棋子不会走出棋盘
    if x >= 0 and x < bdSize:
        return True
    else:
        return False


def knightGraph(bdSize):          #构建骑士图
    ktGraph = Graph()
    for row in range(bdSize):       #遍历每个格子
        for col in range(bdSize):
            nodeId = posToNodeId(row,col,bdSize)    #格子id
            newPositions = genLegalMoves(row,col,bdSize)    #将军单步合法走棋
            for e in newPositions:                  #遍历将军棋子走的八个位置
                nid = posToNodeId(e[0],e[1],bdSize) #走过格子后的位置
                ktGraph.addEdge(nodeId,nid)         #为将军棋子走过的位置添加边
    return ktGraph

def posToNodeId(row, col, bdSize):  #骑士图每个格子的位置
    return row*bdSize+col

def knightTour(n,path,u,limit):     #深度优先算法（图和栈思维） n：层次；path：路径；u；当前顶点；limit：搜索总深度
    u.setColor('gray')
    path.append(u)          #当前顶点加入路径（压栈）
    if n < limit:
        nbrList = list(u.getConnections())  #对所有合法移动逐一深入搜索
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == "white":    #选择白色未经过的顶点深入搜索
                done = knightTour(n+1,path,nbrList[i],limit)    #递归调用，层级加1，深入搜索
            i = i + 1
        if not done:        #都无法完成总深度，回溯，试本层下一个顶点
            path.pop()      #出栈
            u.setColor('white')
    else:
        done = True     #最小结束条件
    return done


def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c, v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


def knightTourBetter(n, path, u, limit):  # use order by available function
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = orderByAvail(u)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n + 1, path, nbrList[i], limit)
            i = i + 1
        if not done:  # prepare to backtrack
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done

kg = knightGraph(5)

thepath = []
start = kg.getVertex(2)
print(start)
knightTour(0,thepath,start,24)
for v in thepath:
    print(v.getId())