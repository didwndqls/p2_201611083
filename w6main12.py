def List():
    x=list()
    for i in range(0,1001):
        if (i%4==0 and i%5!=0):
            x.append(i)
    print x
    print "---------------------------------------------------------------------"
    

def sumList(aList):
    x=list()
    for i in range(0,aList):
        if (i%4==0 and i%5!=0):
            x.append(i)
    mysum=0
    for j in range(0,len(x)):
        mysum=mysum+x[j]
    return mysum

def lab6():
    List()
    aList=1001
    labsum=sumList(aList)
    print labsum
def main():
    lab6()


if __name__=="__main__":
        main()
        
wn=raw_input()