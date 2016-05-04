import matplotlib 
import matplotlib.pyplot as plt
myhome=set() 
friendhome=set() 
myhome={'TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'}
friendhome={'coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'}  
 
 
def charCount(word): 
    d=dict() 
    for c in word: 
        if c not in d: 
            d[c]=1 
        else: 
            d[c]=d[c]+1 
    print d 
    plt.bar(range(0,len(d)),d.values(), align='center') 
    plt.xticks(range(0,len(d)),list(d.keys())) 
    plt.show() 

def countDigitsLetters(word):    
    d={"word":0, "num":0}  
    for c in word:  
        if c.isdigit()==True:  
            d["num"]+=1  
        elif c.isalpha()==True:  
            d["word"]+=1  
    print d  
    plt.bar(range(0,len(d)),d.values(), align='center')  
    plt.xticks(range(0,len(d)),list(d.keys()))  
    plt.show() 

def Mine():
    print 'What is only in my house?', myhome.difference(friendhome)
def Yours():
    print 'What is only in friend house?', friendhome.difference(myhome)
def Both(): 
    print 'What is in my house and friend house?', myhome.intersection(friendhome)
def All(): 
    print 'What is in my house or friend house?', myhome.union(friendhome)
def Count(): 
    d=dict() 
    for i in myhome: 
        if i not in d: 
            d[i]=1 
        else: 
            d[i]+=1 
    for i in friendhome: 
        if i not in d: 
            d[i]=1 
        else: 
            d[i]+=1 
    print d         
 
def lab9A(): 
    word = 'sangmyung university' 
    charCount(word)

def lab9B():
    word = '7 hongjidong'
    countDigitsLetters(word)

def lab9C():
    Mine()
    Yours()
    Both()
    All()
    Count()

def main(): 
    lab9A()
    lab9B()
    lab9C() 
    raw_input() 

 
if __name__=="__main__": 
    main() 
