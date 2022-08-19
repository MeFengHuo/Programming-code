#递归例子之汉诺塔
def moveTower(height,fromPole,toPole,withPole):
    if height >= 1:                             #最小结束条件
        moveTower(height-1,fromPole,withPole,toPole)   #减小规模，调用自身
        moveDisk(height,fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(disk,fromPole,toPole):
    print(f"Moving disk[{disk}] from {fromPole} to {toPole}")

moveTower(4,"A","B","C")
