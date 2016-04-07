def leap():
    Year=input("Please input any year!:")
    if ((Year%4==0) and (Year%100!=0 or Year%400==0)):
        print Year, "is leap year."
    else:
        print Year, "is not leap year."
    wn=raw_input()
    
"""
start
:please input any year!:;
if ((year%4==0) and (year%100!=0 or year%400==0)) then (yes)
:print "This year is leap year.";
else (no)
:print "This year is not leap year.";
endif
stop
"""




def updown():
    import random
    print "Welcome to updown game!"
    Max=input("please set Max number range in the game:")
    rn=random.randrange(1,Max+1,1)
    pn=0
    tn=0
    print"Let's play up&down game!!"
    while(rn!=pn):
        pn=input("Input the number between 1 and Max number:")
        tn=tn+1
        if (rn>pn):
            print"up"
        elif (rn<pn):
            print"down"
        elif (rn==pn):
            print "You tried to", tn ,"times. And it's correct answer!!"
    wn=raw_input()    
        
"""
start
:Let's play up&down game;
:please set max number range in the game:;
:correct number=rn
player number=pn
try number=tn;
:tn=0;
while(play)
:tn=tn+1;
:input pn:;
if(pn < rn) 
:up;
elseif(pn>rn)
:down;
elseif(pn==rn)
:correct;
endif
endwhile(pn==rn)
:You tried to tn times. And it is correct answer!;
stop
"""

def lab6():
    leap()
    updown()
    
def main():
    lab6()
    
if __name__=="__main__":
    main()