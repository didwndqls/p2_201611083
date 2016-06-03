import math
import turtle
import time
wn=turtle.Screen() 
turtle.setup(800,600) 
t1=turtle.Turtle() 
t1.speed(10)
t2 = turtle.Turtle() 
t2.shape("turtle") 
t2.color("Green") 
t2.penup()
location=[(-300,-600),(-200,-600),(100,-600),(200,-600),(300,-600)]
t3=turtle.Turtle()
t3.speed(10)
t3.penup()
t3.goto(0,-500)
t4=turtle.Turtle()
t4.speed(10)
t4.penup()
t4.goto(0,-500)
t5=turtle.Turtle()
t5.speed(10)
t5.penup()
t5.goto(0,-500)
t6=turtle.Turtle()
t6.speed(10)
t6.penup()
t6.goto(0,-500)
t7=turtle.Turtle()
t7.speed(10)
t7.penup()
t7.goto(0,-500)



 
size=100 
turnby=90 
def square(): 
    t1.setheading(0) 
    for i in range(0,4): 
        t1.fd(size) 
        t1.right(turnby) 
def circle():
    t1.circle(50)
 
def S(): 
    t1.setheading(0) 
    t1.back(60) 
    t1.right(turnby) 
    t1.fd(30) 
    t1.left(turnby) 
    t1.fd(60) 
    t1.right(turnby) 
    t1.fd(30) 
    t1.right(turnby) 
    t1.fd(60)
def S1(): 
    t3.setheading(0) 
    t3.back(60) 
    t3.right(turnby) 
    t3.fd(30) 
    t3.left(turnby) 
    t3.fd(60) 
    t3.right(turnby) 
    t3.fd(30) 
    t3.right(turnby) 
    t3.fd(60)
    t3.penup()
    t3.goto(location[0]) 
def O(): 
    t1.setheading(0) 
    for i in range(0,8): 
        t1.fd(30) 
        t1.right(45)
def O1(): 
    t4.setheading(0) 
    for i in range(0,8): 
        t4.fd(30) 
        t4.right(45)
    t4.penup()
    t4.goto(location[1])
def C(): 
    t1.setheading(180) 
    for i in range(0,5): 
        t1.fd(30) 
        t1.left(45)
def C1(): 
    t5.setheading(180) 
    for i in range(0,5): 
        t5.fd(30) 
        t5.left(45)
    t5.setheading(180)
    for i in range(0,5):
        t5.fd(30)
        t5.right(45)
    t5.penup()
    t5.goto(location[2])
def E(): 
    t1.setheading(180) 
    for i in range(0,2): 
        t1.fd(60) 
        t1.left(turnby) 
    t1.fd(60) 
    t1.back(60) 
    t1.left(turnby) 
    t1.fd(30) 
    t1.right(turnby) 
    t1.fd(60)
def E1(): 
    t6.setheading(180) 
    for i in range(0,2): 
        t6.fd(60) 
        t6.left(turnby) 
    t6.fd(60) 
    t6.back(60) 
    t6.left(turnby) 
    t6.fd(30) 
    t6.right(turnby) 
    t6.fd(60)
    t6.penup()
    t6.goto(location[3]) 
def R(): 
    t1.setheading(turnby) 
    for i in range(0,2): 
        t1.fd(60) 
        t1.right(turnby) 
    t1.fd(30) 
    t1.right(turnby) 
    t1.fd(60) 
    t1.left(153) 
    t1.fd(67.082)
def R1(): 
    t7.setheading(turnby) 
    for i in range(0,2): 
        t7.fd(60) 
        t7.right(turnby) 
    t7.fd(30) 
    t7.right(turnby) 
    t7.fd(60) 
    t7.left(153) 
    t7.fd(67.082)
    t7.back(67.082)
    t7.setheading(270)
    t7.fd(30)
    t7.penup()
    t7.goto(location[4])  

def drawsquare():
    t1.pendown()
    square()
    t1.penup()
def drawcircle(): 
    t1.pendown() 
    circle() 
    t1.penup()
def downline():
    t1.pendown()
    t1.pencolor("black")
    t1.setheading(0)
    t1.fd(85)
    t1.penup() 

 
def box(): 
    t1.penup() 
    t1.goto(-300,150) 
    t1.pencolor("red")
    drawcircle() 
    t1.goto(-270,230) 
    t1.pendown() 
    E() 
    t1.penup() 
    t1.goto(-200,250)
    t1.pencolor("blue") 
    drawsquare() 
    t1.goto(-164.857,235) 
    t1.pendown() 
    O() 
    t1.penup() 
    t1.goto(0,150) 
    t1.pencolor("orange")
    drawcircle() 
    t1.goto(25,235) 
    t1.pendown() 
    C() 
    t1.penup() 
    t1.goto(100,250)
    t1.pencolor("red") 
    drawsquare() 
    t1.goto(120,170) 
    t1.pendown() 
    R() 
    t1.penup() 
    t1.goto(300,150) 
    t1.pencolor("blue")
    drawcircle() 
    t1.goto(350,220) 
    t1.pendown() 
    S()
def drawline():
    t1.penup()
    t1.goto(-380,-200)
    downline()
    t1.goto(-245,-200)
    downline()
    t1.goto(-110,-200)
    downline()
    t1.goto(25,-200)
    downline()
    t1.goto(160,-200)
    downline()
    t1.goto(295,-200)
    downline()
myfile=raw_input("input your file name ex)doorcoords.txt:")
openfile=open(myfile)
coords=list()
for line in openfile:
    line1=line.split(',')
    coords.append([(line1[0],line1[1]),(line1[2],line1[3]),(line1[4],line1[5]),(line1[6],line1[7]),(line1[8],line1[9]),(line1[10],line1[11]),(line1[12],line1[13]),(line1[14],line1[15]),(line1[16],line1[17].strip())])
    print coords
openfile.close()

def drawdoor(coords):
    for coord in coords:
        x1=int(coord[0][0])
        x2=int(coord[1][0])
        x3=int(coord[2][0])
        x4=int(coord[3][0])
        x5=int(coord[4][0])
        x6=int(coord[5][0])
        x7=int(coord[6][0])
        x8=int(coord[7][0])
        x9=int(coord[8][0])
        y1=int(coord[0][1])
        y2=int(coord[1][1])
        y3=int(coord[2][1])
        y4=int(coord[3][1])
        y5=int(coord[4][1])
        y6=int(coord[5][1])
        y7=int(coord[6][1])
        y8=int(coord[7][1])
        y9=int(coord[8][1])
        t1.penup()
        t1.goto(x1,y1)
        t1.pendown()
        t1.pencolor("black")
        t1.goto(x2,y2)
        t1.goto(x3,y3)
        t1.goto(x4,y4)
        t1.goto(x5,y5)
        t1.goto(x6,y6)
        t1.goto(x7,y7)
        t1.goto(x8,y8)
        t1.goto(x4,y4)
        t1.penup()
        t1.goto(x9,y9)
        t1.pendown()
        t1.circle(3)
box()
drawdoor(coords)
drawline() 
t1.penup() 
t1.goto(1000,1000)

co1=(-300,200)
co2=(0,200)
co3=(300,200)

def isincircle1(curpos,co1):
    if math.sqrt(math.pow(curpos[0]-co1[0],2)+math.pow(curpos[1]-co1[1],2))<=50 and t3.pos()==(location[0]) and t4.pos()==(location[1]) and t5.pos()==(location[2]):
        t6.penup()
        t6.goto(235,-120)
        t6.pendown()
        t6.pencolor("green")
        E1()
        print "Go to R"
def isincircle2(curpos,co2):
    if math.sqrt(math.pow(curpos[0]-co2[0],2)+math.pow(curpos[1]-co2[1],2))<=50 and t3.pos()==(location[0]) and t4.pos()==(location[1]):
        t5.penup()
        t5.goto(-40,-117)
        t5.pendown()
        t5.pencolor("Purple")
        C1()
        t5.penup()
        t5.goto(95,-117)
        t5.pendown()
        t5.pencolor("Purple")
        C1()
        print "Go to E"
def isincircle3(curpos,co3):
    if math.sqrt(math.pow(curpos[0]-co3[0],2)+math.pow(curpos[1]-co3[1],2))<=50:
        t3.penup()
        t3.goto(-308,-130)
        t3.pendown()
        t3.pencolor("red")
        S1()
        print "Go to O"

coord1=[(-200,150),(-100,250)]
xs1=coord1[0][0]
xe1=coord1[1][0]
ys1=coord1[0][1]
ye1=coord1[1][1]
coord2=[(100,150),(200,250)]
xs2=coord2[0][0]
xe2=coord2[1][0]
ys2=coord2[0][1]
ye2=coord2[1][1]

def isinsquare1(curpos):
    if xs1<=curpos[0]<=xe1 and ys1<=curpos[1]<=ye1 and t3.pos()==(location[0]):
        t4.penup()
        t4.goto(-217.5,-117.5)
        t4.pendown()
        t4.pencolor("orange")
        O1()
        print "Go to C"
        
def isinsquare2(curpos):
    if xs2<=curpos[0]<=xe2 and ys2<=curpos[1]<=ye2 and t3.pos()==(location[0]) and t4.pos()==(location[1]) and t5.pos()==(location[2]) and t6.pos()==(location[3]):
        t7.penup()
        t7.goto(308,-180)
        t7.pendown()
        t7.pencolor("blue")
        R1()
def finish():
    if t3.pos()==(location[0]) and t4.pos()==(location[1]) and t5.pos()==(location[2]) and t6.pos()==(location[3]) and t7.pos()==(location[4]):
        print "good job!"
        print "Go to the Door!!"
coord3=[(300,-35),(350,35)]
xs3=coord3[0][0]
xe3=coord3[1][0]
ys3=coord3[0][1]
ye3=coord3[1][1]
def quit(curpos):
    if t3.pos()==(-300,-600) and t4.pos()==(-200,-600) and t5.pos()==(100,-600) and t6.pos()==(200,-600) and t7.pos()==(300,-600) and xs3<=curpos[0]<=xe3 and ys3<=curpos[1]<=ye3:
        wn.bye()
def record():
    played=open('record.txt','a')
    msg=time.strftime('%Y.%m.%d-%H:%M:%S')
    print msg+'\t'+"Player Coordinate Position is"+'\t'+str(t2.pos())
    played.write('\n'+msg+'\t'+"Player Coordinate Position is"+'\t'+str(t2.pos()))
    played.close()
 
def k1(): 
    t2.forward(45)
    curpos=t2.pos()
    isincircle1(curpos,co1)
    isincircle2(curpos,co2)
    isincircle3(curpos,co3)
    isinsquare1(curpos)
    isinsquare2(curpos)
    finish()
    record()
    quit(curpos)
def k2():   
    t2.left(45) 
def k3(): 
    t2.right(45) 
def k4(): 
    t2.back(45)
    curpos=t2.pos()
    isincircle1(curpos,co1)
    isincircle2(curpos,co2)
    isincircle3(curpos,co3)
    isinsquare1(curpos)
    isinsquare2(curpos)
    finish()
    record()
    quit(curpos)
def addkey():
    wn.onkey(k1, "Up") 
    wn.onkey(k2, "Left")
    wn.onkey(k3, "Right") 
    wn.onkey(k4, "Down")
def mousegoto(x,y):
    t2.setpos(x,y)
    curpos=t2.pos()
    isincircle1(curpos,co1)
    isincircle2(curpos,co2)
    isincircle3(curpos,co3)
    isinsquare1(curpos)
    isinsquare2(curpos)
    finish()
    record()
    quit(curpos)
def addmouse(): 
    wn.onclick(mousegoto) 

addkey()
addmouse()

  

wn.listen() 
 
 
print "Let's Play Soccer Game!"
print "S,O,C,C,E,R alphabetical order, using the arrow keys, place the turtle in shape"
print ">>>>>You should go first to the S"
print "-------------------------------------------------------"
print "" 
turtle.mainloop() 
