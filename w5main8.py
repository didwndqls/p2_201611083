Weight=input("please enter your weight(kg):")
Height=input("please enter your height(m):")
BMI=Weight/(Height*Height)
print BMI
if (BMI<=18.5):
    print "low weight"
elif (18.5<BMI<25.0):
    print "normal weight"
elif (25.0<=BMI<30.0):
    print "over weight"
elif (30.0<=BMI):
    print "obesity"
else:
    print "Error"