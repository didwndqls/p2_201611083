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

#바람개비 그리기 다이어그램  
 %%plantuml  
 @startuml 
  
start  
 :set size, bigger, sides, angle;  
 repeat  
 if (i is multiples of 2) then  
     :size=existing size+bigger;  
 endif  
 :t1.fd(size);  
 :t1.right(angle);  
 repeat while(sides)  
 stop  
 @enduml  
