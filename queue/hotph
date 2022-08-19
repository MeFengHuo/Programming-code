#队列应用——热土豆
from queue import Queue

def hotPhoto(namelist,num):
    simqueue = Queue()
    for name in namelist:       #将参数列表元素加入到队列
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())    #将队列队首出队后再添加到队尾

        simqueue.dequeue()      #按队列出队的方式出到第num个数据项的时候，数据项不再添加到队尾

    return simqueue.dequeue()

# print(hotPhoto(["Bill","David","Susan","Jane","Kent","Brad"],7))
namelist = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
num = 7
for n in range(len(namelist)*num):
    if namelist != []:
        print(hotPhoto(namelist, num))
        namelist.remove(hotPhoto(namelist,num))

