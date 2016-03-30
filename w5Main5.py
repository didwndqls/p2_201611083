marksTmp = raw_input('성적을 입력하세요 (0~100)') 
marks = float(marksTmp) 
print "입력 값은",marks 
if(90<=marks<=100): 
    print "Grade is A" 
elif(80<=marks<90): 
    print "Grade is B" 
elif(70<=marks<80): 
    print "Grade is C" 
elif(60<=marks<70): 
    print "Grade is D" 
else: 
    print "Grade is F"