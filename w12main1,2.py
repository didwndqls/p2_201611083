import os 
mydir=os.getcwd() 
 
 
def homework1(): 
    filename=raw_input("Input your filename(ex:python.txt):") 
    myfilename=os.path.join(mydir,filename) 
    try: 
        myfile=open(myfilename, 'r') 
        contents=myfile.readlines() 
        for i in range(0,len(contents)): 
           if contents[i].find('Python') >= 0: 
                print contents[i] 
        myfile.close() 
    except IOError as e: 
        print e 

 
def homework2(): 
    file=open('output.txt', 'w') 
    line1='first line\n' 
    file.write(line1) 
    line2='second line\n' 
    file.write(line2) 
    line3='third line' 
    file.write(line3) 
    file.close() 
    myfile2=open('output.txt', 'r') 
    contents2=myfile2.readlines() 
    for a in range(0,len(contents2)): 
        if contents2[a].find('l') >= 0: 
            result = contents2[a].split() 
        for b in range(0,len(result)): 
            if result[b].find('l') >= 0: 
                print result[b].upper() 
    myfile2.close() 
      
def lab12(): 
    print "Homework1"
    print ""
    homework1()
    print "------------------------------------------------------------------------------------------------" 
    print "Homework2"
    print ""
    homework2() 


def main(): 
    lab12() 
    raw_input() 

if __name__=="__main__": 
    main() 
