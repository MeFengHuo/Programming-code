'''
基本数据结构：图graph>>重在由一些基本元素构造而成，如点，线段等
图是由顶点Vertex（或者叫节点node）和边Edge（或者弧Arc）组成
术语：
 顶点vertex：是图组成的基本元素，具有标识key，还可以携带数据项payload
 边edge：表示两个顶点之间的关系，边连接两个顶点；边可以是有向或者无向的，相应的图称为“无向图”和“有向图”
 权重Weight：表达一个顶点到另一个顶点的“代价”，可以给边赋权，具有权重的图称为赋权图，在不同的网络中有不同的含义：
    例如公交网络中两个站点之间的距离，通行时间和票价都可以作为边的权重
 图可以定义为 G = （V，E）
    其中V是顶点的集合，E是边的集合
    E中的每条边e = （v0，v1），其中v0和v1是图中的两个顶点
    表示赋权图：则需要在每条边中添加权重分量，即：e = （v0，v1，w），其中v0和v1是两个顶点，w是权重分量
 路径Path：是由边依次连接起来的顶点序列；无权路径的长度是边的数量；带权路径的长度是所有序列边的权重和
 圈Cycle：圈是首尾顶点相同的路径
    如果有向图中不存在任何圈，则称为 “有向无圈图”directed acyclic graph:DAG"
抽象数据类型:ADT Graph（ADT：abstract data type>>抽象数据类型）
  实现方式主要两种：
  邻接矩阵adjacency matrix
  邻接表adjacency list
'''
class Vertex:           #对象顶点
    def __init__(self,key):     #初始化顶点
        self.id = key           #顶点id
        self.connectedTo = {}   #顶点id连接其他的顶点的边，例：v0 = {v1:1，}是指v0和v1连接的边，权重为1

    def addNeighbor(self,nbr,weight=0):     #方法：给顶点添加从self到nbr的边，权重默认为0 （neighbor：邻居，邻近的）
        self.connectedTo[nbr] = weight

    def __str__(self):          #字符串特殊方法：打印字符串，例：打印出 v0 连接到 v1，v2
        return str(self.id) + "connectedTo: " + str([x.id for x in self.connectedTo])

    def getConnections(self):    #方法：获得连接的顶点
        return self.connectedTo.keys()

    def getId(self):            #方法：获得当前顶点
        return self.id

    def getWeight(self,nbr):    #方法：获得权重
        return self.connectedTo[nbr]

class Graph:                    #对象图
    def __init__(self):         #初始化图
        self.vertexList = {}    #顶点列表：用字典表示
        self.numVertices = 0    #顶点数量

    def addVertex(self,key):    #方法：添加新顶点
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex

    def getVertex(self,n):      #方法：获得顶点
        if n in self.vertexList:
            return self.vertexList[n]
        else:
            return None

    def __contains__(self, item):   #特殊方法：in操作
        return item in self.vertexList

    def addEdge(self,fromVertex,toVertex,wight=0):   #方法：添加带权重的边
        if fromVertex not in self.vertexList:
            nv = self.addVertex(fromVertex)
        if toVertex not in self.vertexList:
            nv = self.addVertex(toVertex)
        self.vertexList[fromVertex].addNeighbor(self.addVertex(toVertex),wight)

    def getVertices(self):          #方法：获得顶点
        return self.vertexList.keys()

    def __iter__(self):             #特殊方法：迭代器>>可以用for遍历
        return iter(self.vertexList.values())

g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.vertexList)
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
for v in g:
    for w in v.getConnections():
        print("(%s,%s)"%(v.getId(),w.getId()))



