def saveTracks():
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    t1.speed(3)
    t1.pencolor("RED")
    t1.shape("turtle")
    t1.penup()
    mytracks=list()
    t1.goto(-315,330)
    mytracks.append(t1.pos())
    t1.pendown()
    t1.right(90)
    t1.forward(180)
    mytracks.append(t1.pos())
    t1.left(90)
    t1.forward(230)
    mytracks.append(t1.pos())
    t1.right(90)
    t1.forward(230)
    mytracks.append(t1.pos())
    t1.left(90)
    t1.forward(400)
    mytracks.append(t1.pos())
    t1.right(90)
    t1.forward(260)
    mytracks.append(t1.pos())
    return mytracks


def replayTracks(mytracks):
    for i in mytracks:
        print i
        
def lab7():
    mytracks=saveTracks()
    replayTracks(mytracks)
    
def main():
    lab7()
    input()
    
if __name__=="__main__":
    main()