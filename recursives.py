#用递归（recursive）画图
import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle,linelen):       #定义螺旋（spiral）函数
    if linelen > 0:
        myTurtle.forward(linelen)
        myTurtle.right(90)
        drawSpiral(myTurtle,linelen-5)

# drawSpiral(myTurtle,100)
# myWin.exitonclick()

def tree(branchLen,t):                  #定义二叉树函数
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myW = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myW.exitonclick()

main()