import time
def homework1():
    file=open('output.txt', 'w')
    line1='first line\n'
    file.write(line1)
    line2='second line\n'
    file.write(line2)
    line3='third line'
    file.write(line3)
    file.close()
    msg='[YJB edited {0}]'.format(time.strftime('%Y-%m-%d %H:%M:%S'))
    fin=open('output.txt', 'r')
    fout=open('outputUpper.txt','w')
    for line in fin:
        words=line.split()
        fout.write(msg)
        for word in words:
            if word == 'line':
                fout.write('\t')    
                word=word.upper()
            fout.write(word)
        fout.write('\n')
    fin.close()
    fout.close()
    
def homework2():
    data=[1,2,3,4,5,6,7,8,9,10]
    fout=open('number.txt', 'w')
    for i in data:
        str="{0}\t".format(i)
        fout.write(str)
        if i%2==0:
            fout.write('\n')
    fout.close()

def lab12():
    homework1()
    homework2()

def main():
    lab12()
    raw_input()

if __name__=="__main__":
    main()