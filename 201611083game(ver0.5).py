import turtle
wn=turtle.Screen()
turtle.setup(800,600)
t1=turtle.Turtle()
t1.speed(10)


size=100
turnby=90
def square():
    t1.setheading(0)
    for i in range(0,4):
        t1.fd(size)
        t1.right(turnby)
    for i in range(0,4):
        t1.right(turnby)
        t1.fd(20)
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
def O():
    t1.setheading(0)
    for i in range(0,8):
        t1.fd(30)
        t1.right(45)
def C():
    t1.setheading(180)
    for i in range(0,5):
        t1.fd(30)
        t1.left(45)
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
def P():
    t1.pendown()
    square()
    t1.penup()

def box():
    t1.penup()
    t1.goto(-350,250)
    P()
    t1.goto(-270,230)
    t1.pendown()
    E()
    t1.penup()
    t1.goto(-200,250)
    P()
    t1.goto(-164.857,235)
    t1.pendown()
    O()
    t1.penup()
    t1.goto(-50,250)
    P()
    t1.goto(25,235)
    t1.pendown()
    C()
    t1.penup()
    t1.goto(100,250)
    P()
    t1.goto(120,170)
    t1.pendown()
    R()
    t1.penup()
    t1.goto(250,250)
    P()
    t1.goto(330,230)
    t1.pendown()
    S()
box()
t1.penup()
t1.goto(1000,1000)

t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("Green")
t2.penup()

def k1():
    t2.forward(45)
def k2():  
    t2.left(45)
def k3():
    t2.right(45)
def k4():
    t2.back(45)
wn.onkey(k1, "Up")

wn.onkey(k2, "Left")

wn.onkey(k3, "Right")

wn.onkey(k4, "Down")



wn.listen()

raw_input("You want end game press enter")

