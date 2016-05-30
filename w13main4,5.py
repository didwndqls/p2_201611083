import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def homework():
    file1=raw_input("Append file ex)python.txt: ")
    file2=raw_input("Read file ex)number.txt: ")
    try:
        fin1=open(file1, 'a')
        fin2=open(file2, 'r')
        for line in fin2:
            fin1.write(line)
        fin1.close()
        fin2.close()
    except Exception as e:
        print e


def getCoordsFromFile(myfile):
    filehome=open(myfile)
    coords=list()
    for line in filehome:
        line1=line.split(',')
        print [(line1[0],line1[1]), (line1[2],line1[3].strip())]
        coords.append([(line1[0],line1[1]), (line1[2],line1[3].strip())])
    return coords
    filehome.close()


def drawSquareWithCoords(coords):
    for coord in coords:
        x1=int(coord[0][0])
        x2=int(coord[1][0])
        y1=int(coord[0][1])
        y2=int(coord[1][1])
        print x1,y1,x2,y2
        t1.penup()
        t1.goto(x1,y1)
        t1.pendown()
        t1.setheading(0)
        for i in range(0,4):
            t1.fd(x1-x2)
            t1.rt(90)
    

def lab4():
    homework()
def lab5():
    myfile=raw_input("Input filename ex)reccoords.txt: ")
    coords=getCoordsFromFile(myfile)
    drawSquareWithCoords(coords)

def main():
    lab4()
    lab5()
    input()


if __name__=="__main__":
    main()
