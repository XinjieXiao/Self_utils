from turtle import *
from random import *
import turtle as t
import time
import math
from math import cos, sin, atan, sqrt
import numpy as np
 
t.screensize(bg='black')  # 定义背景颜色
 
 
# 心函数
def loving_heart(r):
    l = 2 * r
    t.left(45)
    t.forward(l)
    t.circle(r, 180)
    t.right(90)
    t.circle(r, 180)
    t.forward(l)
 
 
# 星函数
def loving_star(n):
    for i in range(5):
        t.forward(n / 5)
        t.right(144)
        t.forward(n / 5)
        t.left(72)
 
 
# 绘图方法
def Rightdraw(Range, Fd, Right):
    for i in range(Range):  # Range循环次数
        fd(Fd)  # 向前Fd个距离
        right(Right)  # 在当前行进方向再向右偏转Right度
 
 
def Leftdraw(Range, Fd, Left):
    for i in range(Range):  # Range循环次数
        fd(Fd)  # 向前Fd个距离
        left(Left)  # 在当前行进方向再向右偏转Right度
 
 
# 背景改为黑色
screensize(bg='black')
 
 
# 重设海龟位置
def changeMypos(x, y, range=heading(), Fd=0):
    penup()
    goto(x, y)
    seth(range)
    fd(Fd)
    pendown()
 
 
def drawBranch(x, y, size=1):
    changeMypos(x, y)
    Leftdraw(6, 3, 9)
    seth(0)
    Rightdraw(6, 3, 9)
    seth(0)
    fd(6)
 
 
# 画五角星
def drawStar(x, y, Range, size):
    pensize(1)
    color("red", "yellow")
    begin_fill()
    changeMypos(x, y, Range)
    for i in range(5):  # 画五角星
        forward(10 * size)
        right(144)  # 五角星的角度
        forward(10 * size)
        left(72)  # 继续换角度
    end_fill()
    right(126)
 
 
# 绘制雪花
def drawSnow():
    hideturtle()
    speed(0)
    pencolor("white")
    pensize(2)
    for i in range(80):  # 雪花数量
        changeMypos(randint(-248, 248), randint(-100, 248))
        petalNumber = 6  # 雪花花瓣数为6
        snowSize = int(randint(2, 10))
        for j in range(petalNumber):
            fd(snowSize)
            backward(snowSize)
            right(360 / petalNumber)
 
 
# 圣诞袜子
def drawSock(x, y, range, size=1):
    # 绘制袜子的白边
    pensize(1)
    changeMypos(x, y, range)
    color("black", "white")
    begin_fill()
    fd(20 * size)
    circle(3 * size, 180)
    fd(20 * size)
    circle(3 * size, 180)
    end_fill()
 
    # 绘制袜子的下半部分
    color("white", "red")
    begin_fill()
    startx = x + 2 * size * math.cos(math.radians(range))
    starty = y + 2 * size * math.sin(math.radians(range))
    finalx = x + 18 * size * (math.cos(math.radians(range)))
    finaly = y + 18 * size * (math.sin(math.radians(range)))
    changeMypos(startx, starty, range - 90)
    fd(20 * size)  # 圆弧距离白边40
    seth(180 + range)
    fd(5 * size)  # 向袜子头延伸10
    circle(7 * size, 180)  # 袜子头处的半圆形
    fd(21 * size)  # 袜子宽42
    seth(90 + range)
    d = distance(finalx, finaly)  # 找到袜子底部与白边的距离
    fd(d)
    seth(range + 180)
    fd(16 * size)
    end_fill()
 
 
# 圣诞帽
def drawHat(x, y, range, size=1):
    # 绘制帽白边
    pensize(1)
    changeMypos(x, y, range)
    color("white", "white")
    begin_fill()
    fd(20 * size)
    circle(-3 * size, 180)
    fd(20 * size)
    circle(-3 * size, 180)
    end_fill()
    # 绘制帽子上半部分
    color("white", "red")
    begin_fill()
    startx = x + 2 * size * math.cos(math.radians(range))
    starty = y + 2 * size * math.sin(math.radians(range))
    finalx = x + 18 * size * (math.cos(math.radians(range)))
    finaly = y + 18 * size * (math.sin(math.radians(range)))
    changeMypos(startx, starty, range + 90)
    Rightdraw(18, 2 * size, 7)
    seth(190)
    Leftdraw(9, 2 * size, 8)
    goto(finalx, finaly)
    goto(startx, starty)
    end_fill()
    # 绘制圣诞帽上的小球
    changeMypos(startx, starty, range + 90)
    Rightdraw(18, 2 * size, 7)
    begin_fill()
    color("white", "white")
    circle(-2.5 * size)
    end_fill()
 
 
# 绘制彩带
def drawRibbon(x, y, range, size):
    begin_fill()
    color("red", "red")
    seth(range + 40)
    fd(15 * size * math.tan(math.radians(range + 40)))
    seth(range + 90)
    fd(20 / 3 * size)
    seth(range - 140)
    fd(15 * size * math.tan(math.radians(range + 40)))
    seth(range - 90)
    fd(20 / 3 * size)
    end_fill()
 
 
# 圣诞糖果
def drawCandy(x, y, range, size):
    # 绘制糖体
    pensize(1)
    changeMypos(x, y, range)
    color("white", "white")
    begin_fill()
    startx = x + 2 * size * math.cos(math.radians(range))
    starty = y + 2 * size * math.sin(math.radians(range))
    finalx = x + 8 * size * (math.cos(math.radians(range)))
    finaly = y + 8 * size * (math.sin(math.radians(range)))
    changeMypos(startx, starty, range + 90, 40 * size)
    circle(-40 / 3 * size, 180)
    circle(-8 / 3 * size, 180)
    circle(22 / 3 * size, 180)
    goto(finalx, finaly)
    goto(startx, starty)
    end_fill()
    # 绘制下面三条彩带
    color("white")
    changeMypos(startx, starty, range + 90)
    fd(10 / 3 * size)
    drawRibbon(xcor(), ycor(), range, size)
    changeMypos(xcor(), ycor(), range + 90, 13.3 * size)
    drawRibbon(xcor(), ycor(), range, size)
    changeMypos(xcor(), ycor(), range + 90, 13.3 * size)
    drawRibbon(xcor(), ycor(), range, size)
    # 绘制弧线段的彩带
    changeMypos(startx, starty, range + 90, 40 * size)
    circle(-13.3 * size, 55)
    x1 = xcor()
    y1 = ycor()
    begin_fill()
    circle(-13.3 * size, 80)
    right(75)
    fd(6.3 * size)
    right(115)
    circle(7 * size, 85)
    goto(x1, y1)
    end_fill()
 
 
setup(500, 500, startx=None, starty=None)
title("Merry Christmas")
speed(0)
pencolor("green")
pensize(10)
hideturtle()
changeMypos(0, 185, 0)
 
# shape(name= "classic")
 
# # 树顶层
seth(-120)
Rightdraw(10, 12, 2)
changeMypos(0, 185, -60)
 
Leftdraw(10, 12, 2)
 
changeMypos(xcor(), ycor(), -150, 10)
 
# # 第一层的波浪
for i in range(4):
    Rightdraw(5, 7, 15)
    seth(-150)
    penup()
    fd(2)
    pendown()
 
# # 树二层
changeMypos(-55, 70, -120)
Rightdraw(10, 8, 5)
 
changeMypos(50, 73, -60)
Leftdraw(10, 8, 5)
 
changeMypos(xcor(), ycor(), -120, 10)
seth(-145)
pendown()
 
# # 第二层的波浪
for i in range(5):
    Rightdraw(5, 9, 15)
    seth(-152.5)
    penup()
    fd(3)
    pendown()
 
# 树三层
changeMypos(-100, 0, -120)
Rightdraw(10, 6.5, 4.5)
 
changeMypos(80, 0, -50)
Leftdraw(10, 6, 3)
 
changeMypos(xcor(), ycor(), -120, 10)
seth(-145)
 
# # # 第三次的波浪
for i in range(6):
    Rightdraw(5, 9, 15)
    seth(-152)
    penup()
    fd(3)
    pendown()
 
# # 树四层
changeMypos(-120, -55, -130)
Rightdraw(7, 10, 4)
 
changeMypos(100, -55, -50)
Leftdraw(7, 10, 5)
 
changeMypos(xcor(), ycor(), -120, 10)
seth(-155)
 
# # # 第四层的波浪
for i in range(7):
    Rightdraw(5, 9, 13)
    seth(-155)
    penup()
    fd(3)
    pendown()
 
# 树根
changeMypos(-70, -120, -85)
Leftdraw(3, 8, 3)
 
changeMypos(70, -120, -95)
Rightdraw(3, 8, 3)
 
changeMypos(xcor(), ycor(), -170, 10)
Rightdraw(10, 12, 2)
 
# 画树枝
drawBranch(45, -80)
drawBranch(-70, -25)
drawBranch(-20, 40)
 
# 添加挂件
drawHat(-25, 175, -10, 2.5)
drawCandy(-75, -50, -10, 1)  # -10别动了，这个绘制有点烦，我没做转角功能
drawCandy(10, 40, -10, 1.2)
drawStar(110, -90, 80, 1)
drawStar(-120, -100, 50, 1)
drawStar(-90, -50, 20, 1)
drawStar(90, -25, 30, 1)
drawSock(10, -35, -10, 2)
drawSock(-40, 100, 10, 1)
drawStar(-20, 40, 30, 1)
drawStar(10, 120, 90, 1)
 
 
# # 写下署名
t.color("purple")  # 填充颜色
t.up()  # 抬笔
t.goto(130, -240)
t.down()  # 落笔
t.write("苏苏老婆:圣诞节快乐！\n", align='center',font=("Times New Roman", 24, "normal"))

t.hideturtle()
time.sleep(2)
 
# 烟火
WIDTH = 0
HEIGHT = 0
ORI = (0, 0)
COLOR = {'0': '#070920', 'navyblue': '#000080'}
FIRE = []
 
 
def setParam():
    global WIDTH
    global HEIGHT
    global ORI
    global FIRE
    WIDTH = t.window_width()
    HEIGHT = t.window_height()
    ORI = (0, -HEIGHT / 2)
    # gold
    FIRE.append(['white', '#FFD700', '#DAA520', '#BDB76B', ])
    # red
    FIRE.append(['white', '#F08080', '#A0522D', '#DC143C', ])
    # green
    FIRE.append(['white', '#7FFF00', '#32CD32', '#006400', ])
    # cyan
    FIRE.append(['white', '#40E0D0', '#00FFFF', '#008080', ])
    # pink
    FIRE.append(['white', '#FF69B4', '#FF1493', '#8B008B', ])
    # buff
    FIRE.append(['white', '#FFE4C4', '#FFDAB9', '#F0FFF0', ])
    # bluish
    FIRE.append(['white', '#ADD8E6', '#AFEEEE', '#00BFFF', ])
 
 
def dist(a, b):  # 距离
    return ((a - b) * (a - b)).sum()
 
 
def shoot():
    t.tracer(4)  # 在循环中，图形将一次画出4次循环的图
    t.pu()
    target = np.array((np.random.randint(-WIDTH // 6, WIDTH // 6),
                       HEIGHT // 6))  # 都在同一高度
    angle = atan((target - ORI)[1] / (target - ORI)[0])
    if angle < 0:
        angle += math.pi  # 纠正负方向
    unit = np.array([cos(angle), sin(angle)])  # 方向向量
    print('angle: ', angle)
    print('target: ', target)
    # 镜头的顺序坐标
    seq = np.array([ORI, ORI - 55 * unit, ORI - 105 * unit, ORI - 155 * unit])
    t.speed(0)  # 瞬动
    while dist(seq[0], target) > 120:  # 如果没有到达爆炸中心
        seq = seq + 30 * unit
 
        t.goto(seq[1])
        t.pd()
        t.width(3)
        t.pencolor('white')
        t.goto(seq[0])
        t.pu()
 
        t.goto(seq[2])
        t.pd()
        t.width(3)
        t.pencolor('yellow')
        t.goto(seq[1])
        t.pu()
 
        # 清除发射上去的光束尾迹
        t.goto(seq[3])
        t.pd()
        t.width(10)
        t.pencolor(COLOR['0'])
        t.goto(seq[2])
        t.pu()
        time.sleep(0.05)
 
    # 发射上去的光束最后清除
    t.pd()
    t.width(10)
    t.goto(seq[0])
    t.pu()
    time.sleep(0.1)
    return target  # 就在爆炸中心
 
 
def explode(center):
    number = np.random.randint(50, 100)  # 光束数
    colormode = np.random.randint(0, 5)
    unit = np.array([])  # 方向向量
    spd = []  # 每个光束的速度
    seq = []  # 每个波束的顺序坐标
    if colormode <= 1:
        coloridx = [np.random.randint(0, len(FIRE))]
    elif colormode == 2:
        coloridx = [np.random.randint(0, len(FIRE)),
                    np.random.randint(0, len(FIRE))]
    elif colormode == 3:
        coloridx = [np.random.randint(0, len(FIRE)),
                    np.random.randint(0, len(FIRE)),
                    np.random.randint(0, len(FIRE))]
    elif colormode == 4:
        coloridx = []
 
    # 不同大小烟花的步骤
    steps = int((number ** 0.5) * 2)
 
    # 初始化
    for i in range(number):
        angle = np.random.rand() * 2 * math.pi - math.pi
        unit = np.append(unit, [cos(angle), sin(angle)]).reshape(-1, 2)
        seq = np.append(
            seq,
            [center,
             center - 10 * unit[i], center - 50 * unit[i],
             center - 90 * unit[i], center - 130 * unit[i],
             center - 135 * unit[i]]
        )
        spd.append(int(15 + (np.random.rand() - 0.5) * 5))
 
        if colormode <= 1:
            coloridx.append(coloridx[0])
        elif colormode == 2:
            coloridx.append(coloridx[np.random.randint(0, 2)])
        elif colormode == 3:
            coloridx.append(coloridx[np.random.randint(0, 3)])
        elif colormode == 4:
            coloridx.append(np.random.randint(0, len(FIRE)))
 
    seq = seq.reshape([-1, 6, 2]).astype(np.int32)
    t.tracer(0x3f3f3f3f)  # 关闭自动更新，0x3f3f3f3f是一个大数字
 
    for stage in range(steps):
        for i in range(number):
            seq[i] = seq[i] + spd[i] * unit[i]
            seq[i][4] = center
            for cur in range(4):
                t.pu()
                t.goto(seq[i][cur + 1])
                t.pd()
                t.pencolor(FIRE[coloridx[i]][cur])
                t.width(4 - cur)
                t.goto(seq[i][cur])
                t.pu()
        if stage >= 5:  # 等待所有光束就位
            t.update()
            time.sleep(0.04)
 
    # 清除每次绽放的烟花
    for cur in range(4, -1, -1):
        for i in range(number):
            t.pu()
            t.goto(seq[i][cur + 1])
            t.pd()
            t.pencolor(COLOR['0'])
            t.width(100)
            t.goto(seq[i][cur])
            t.pu()
        time.sleep(0.02)
        t.update()
 
 
def main():
    t.setup(700, 750, 100, 0)
    setParam()
    while True:
        point = shoot()
        explode(point)
    exitonclick()  # 在任何位置单击退出
 
 
if __name__ == '__main__':
    main()