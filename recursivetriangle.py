#用递归绘制谢尔宾斯基三角形

import turtle

def drawTriangle(points,color,myTurtle):    #绘制三角形
    # myTurtle = turtle.Turtle()
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):              #获得三角形中线
    return ( (p1[0]+p2[0])/2 , (p1[1]+p2[1])/2 )

def sierpinske(points,degree,myTurtle):         #递归调用自身
    colormap = ["blue","red","green","white","yellow","violet","orange"]
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinske([points[0],
                    getMid(points[0],points[1]),
                    getMid(points[0],points[2])],
                   degree-1,myTurtle)
        sierpinske([points[1],
                    getMid(points[0],points[1]),
                    getMid(points[1],points[2])],
                   degree-1,myTurtle)
        sierpinske([points[2],
                    getMid(points[2],points[1]),
                    getMid(points[0],points[2])],
                   degree-1,myTurtle)

def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-100,-50],[0,100],[100,-50]]
    sierpinske(myPoints,3,myTurtle)
    myWin.exitonclick()

main()

