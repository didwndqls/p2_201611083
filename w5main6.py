import turtle
wn=turtle.Screen()
def play():
    Aplayer=raw_input("A player input Rock, Scissor or Paper:")
    Bplayer=raw_input("B player input Rock, Scissor or Paper:")
    print Aplayer,"vs", Bplayer
    def N(A):
        if(A=="Scissor"):
            return 1
        elif(A=="Rock"):
            return 0
        elif(A=="Paper"):
            return -1
    result= N(Aplayer)- N(Bplayer)    
    if (result==0):
        print "=darw"
    elif (result== -1):
        print "=A player is win!"
    elif (result== 2):
         print "=A player is win!"
    elif (result== -2):
        print "=B player is win!"
    elif (result== 1):  
        print "=B player is win!"
    else:
        print "=Error"
play()
wn.exitonclick()