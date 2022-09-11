#图应用：词梯->从一个单词变换字母变成另一个字母，例：fool->cool->pool->poll
from graph import Graph,Vertex
from queue import Queue

def buildGraph(wordFile):       #创建单词图，两个单词相差一个字母添加一条边
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    #创造一组单词桶，每组单词相差一个字母，例：fool,cool,pool -> _ool
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    #为同一个桶中的单词添加顶点和边
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == "white"):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')

def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

wordgraph = buildGraph("fourletterwords.txt")
bfs(wordgraph,wordgraph.getVertex('FOOL'))
traverse(wordgraph.getVertex('SAGE'))
