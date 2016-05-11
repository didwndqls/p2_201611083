import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()

def keyup():
    t1.fd(50)
def keydown():
    t1.back(50)
def keyleft():
    t1.left(90)
def keyright():
    t1.right(90)
def mousegoto(x,y):
    t1.setpos(x,y)
    (x,y)=t1.pos()
    if -100<=x<=100 and y==200:
        print "great"
def line():
    t2.penup()
    t2.goto(-100,200)
    t2.pendown()    
    t2.fd(200)
    t2.penup()
    t2.goto(1000,1000)
    

def addkeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyleft,"Left")
    wn.onkey(keyright,"Right")
def addmouse():
    wn.onclick(mousegoto)

addkeys()
addmouse()
line()
wn.listen()
turtle.mainloop()
