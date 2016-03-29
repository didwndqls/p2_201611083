import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def makeSwirSquare(size,bigger,sides,angle):
    for i in range(sides):
        if(i%2):
            size=size+bigger
            t1.fd(size)
            t1.right(angle)
makeSwirSquare(10,10,30,90)
wn.exitonclick()
