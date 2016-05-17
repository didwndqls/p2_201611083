import turtle
import math
wn=turtle.Screen()
t1=turtle.Turtle()
wn.bgpic("C:\Users\SAMSUNG\Desktop\miro_converted.gif")

coord = [(120,100),(220,200)]
xs=coord[0][0]
ys=coord[0][1]
xe=coord[1][0]
ye=coord[1][1]

line1=[(50,250),(150,250)]
x1=line1[0][0]-10
y1=line1[0][1]-10
x2=line1[1][0]+10
y2=line1[1][1]+10
pos1=(x1,y1)
pos2=(x2,y2)

line2=[(250,150),(250,250)]
x3=line2[0][0]-10
y3=line2[0][1]-10
x4=line2[1][0]+10
y4=line2[1][1]+10
pos3=(x3,y3)
pos4=(x4,y4)

circlepos=(0,100)
radious=100

def background():
    t1.shape("turtle")
    t1.penup()
    t1.goto(-315,330)
    t1.clear()

def drawSquare():
    t1.penup()
    t1.goto(120,100)
    t1.setheading(0)
    t1.pendown()
    for i in range(0,4):
        t1.fd(100)
        t1.left(90)
    t1.penup()
    t1.goto(-315,330)

def drawLine1():
    t1.setheading(0)
    t1.penup()
    t1.goto(50,250)
    t1.pendown()
    t1.fd(100)
    t1.penup()
    t1.goto(-315,330)

def drawLine2():
    t1.setheading(0)
    t1.penup()
    t1.goto(250,150)
    t1.pendown()
    t1.setheading(0)
    t1.left(90)
    t1.fd(100)
    t1.penup()
    t1.goto(-315,330)

def drawCircle():
    t1.penup()
    t1.home()
    t1.pendown()
    t1.circle(100)
    t1.penup()
    t1.goto(-315,330)


def isinRectangle(coord,curpos):
    if xs<=curpos[0]<=xe and ys<=curpos[1]<=ye:
        t1.color("Red")
        drawSquare()

def isOnLine1(curpos,pos1,pos2):
    if x1<=curpos[0]<=x2 and y1<=curpos[1]<=y2:
        t1.color("Blue")
        drawLine1()

def isOnLine2(curpos,pos3,pos4):
    if x3<=curpos[0]<=x4 and y3<=curpos[1]<=y4:
        t1.color("Orange")
        drawLine2()

def isinCircle(curpos,radious,circlepos):
    if math.sqrt(math.pow(curpos[0]-circlepos[0],2) + math.pow(curpos[1]-circlepos[1],2))<=100:
        t1.color("Green")
        drawCircle()

def Draw():
    background()
    drawSquare()
    drawLine1()
    drawLine2()
    drawCircle()

def keyup():
    t1.fd(50)
    curpos=t1.pos()
    isinRectangle(coord,curpos)
    isOnLine1(curpos,pos1,pos2)
    isOnLine2(curpos,pos3,pos4) 
    isinCircle(curpos,radious,circlepos)

def keydown():
    t1.back(50)
    curpos=t1.pos()
    isinRectangle(coord,curpos)
    isOnLine1(curpos,pos1,pos2)
    isOnLine2(curpos,pos3,pos4) 
    isinCircle(curpos,radious,circlepos)

def keyleft():
    t1.left(90)

def keyright():
    t1.right(90)

def mousegoto(x,y):
    t1.setpos(x,y)
    curpos=t1.pos()
    isinRectangle(coord,curpos)
    isOnLine1(curpos,pos1,pos2)
    isOnLine2(curpos,pos3,pos4) 
    isinCircle(curpos,radious,circlepos)

def addkeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keydown, "Down")
    wn.onkey(keyright, "Right")
    wn.onkey(keyleft, "Left")

def addmouse():
    wn.onclick(mousegoto)

Draw()
addkeys()
addmouse()
wn.listen()
turtle.mainloop()


