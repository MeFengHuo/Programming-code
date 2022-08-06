# 队列应用——模拟打印机任务
from queue import Queue
import random

class Printer:              #创建打印机对象类
    def __init__(self,ppm):     #打印机初始化，生成其属性
        self.pagerate = ppm     #打印机速度
        self.currentTask = None #打印任务
        self.timeRemaining = 0  #打印倒计时

    def tick(self):             #(方法)打印1秒
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining -1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):             #（方法）打印机是否忙？
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):    #打印新作业
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate

class Task:                         #创建（打印作业任务）对象类
    def __init__(self,time):        #初始化（打印作业），生成其属性
        self.timestamp = time       #生成时间戳
        self.pages = random.randrange(1,21)     #打印页数

    def getStamp(self):             #获取时间
        return self.timestamp

    def getPages(self):             #获取打印作业的页数
        return self.pages

    def waitTime(self,currenttime):             #获取等待时间
        return currenttime - self.timestamp    #当前时间-生成时间

def newPrintTask():                 #新生成打印任务，返回值是布尔值
    num = random.randrange(1,181)   #180之1的概率生成新作业
    if num == 180:
        return True
    else:
        return False

def simulation(numSeconds,pagesPerMinute):  #创建(打印过程模拟)函数 俩个参数1打印时间2打印模式(每秒打印速度)
                                            #打印工程模拟用队列实现
    labprinter = Printer(pagesPerMinute)    #生成打印机
    printQueue = Queue()                    #生成打印队列
    waitingtimes = []                       #生成等待时间列表

    for currentSecond in range(numSeconds): #打印过程

        if newPrintTask():
            task = Task(currentSecond)      #生成打印作业任务
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)   #平均打印时间
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))


for i in range(10):
    simulation(3600,5)
