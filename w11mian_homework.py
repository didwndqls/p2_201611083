dataA=[[13.1, 37.1],
     [10.6, 34.6],
     [27.1, 40.0],
     [16.2, 37.8],
     [11.4, 29.8],
     [12.2, 26.5],
     [13.5, 29.7],
     [13.7, 37.6]]
dataB=[[8.7, 1.5],
      [13.4, 1.9],
      [2.9, 1.5],
      [6.8, 0.8],
      [14.8, 4.9],
      [14.9, 4.4],
      [11.1, 2.4],
      [4.1, 1.2]]
sumA=0
sumB=0
for i in dataA:
    sumA=sumA+i[0]+i[1]
for a in dataB:
    sumB=sumB+a[0]+a[1]
print "dataA = "
for b in dataA:
    print b
print "dataB = "
for c in dataB:
    print c
print "dataA sum:",sumA, "// dataB sum:",sumB
print "dataA average:",float(sumA/len(dataA)), "// dataB average:",float(sumB/len(dataB))
input()