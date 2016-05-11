print "Save percentage to add to the Milk Coffee"
print ""
allData=list()
allData=[["Coffee","Water","Milk","Icecream"],
  ["Espresso","No","No","No"],
  ["Long Black","Yes","No","No"],
  ["Flat White","No","Yes","No"],
 ["Cappuccino","No","Yes - Frothy","No"],
  ["Affogato","No","No","Yes"]]
data=allData[1:]
value=0.
for i in data:
    if i[2]=='Yes' or i[2]=='Yes - Frothy':
        value=value+1
result=value/len(data)*100
for a in allData:
    print a

print "The ratio of coffee with milk in?", result,"%"
print "---------------------------------------------------------------------"
print ""
print "Obtaining the average / total of qualitative data"
print ""

score=list()
score=[['English',100],['Math',200],['English',200],['Math',200],['English',100],['Math',300]]
Esum=0.
Msum=0.
for i in score:
    if i[0]=="English":
        Esum+=i[1]
    elif i[0]=="Math":
        Msum+=i[1]
e=0.
m=0.
for b in score:
   if b[0]=="English":
        e+=1
   elif b[0]=="Math":
        m+=1 

for a in score:
    print a
print "English Sum Score Is :", Esum
print "Math Sum Score Is :", Msum
print "English Average Score Is :", Esum/e
print "Math Average Score Is :", Msum/m
print "--------------------------------------------------------------------------"
print ""
print "The Beatles 'Let it be' a word that often appears in the lyrics ?"
print ""
print ""
lyrics=['When I find myself in times of trouble',
'Mother Mary comes to me',
'Speaking words of wisdom let it be',
'And in my hour of darkness',
'She is standing right in front of me',
'Speaking words of wisdom let it be',

'Let it be let it be',
'Let it be let it be',
'Whisper words of wisdom let it be',

'And when the broken-hearted people',
'Living in the world agree',
'There will be an answer let it be',
'For though they may be parted',
'There is still a chance that they will see',
'There will be an answer let it be',

'Let it be let it be',
'Let it be let it be',
'Yeah there will be an answer let it be',
'Let it be let it be',
'Let it be let it be',
'Whisper words of wisdom let it be',

'Let it be let it be',
'Ah let it be yeah let it be',
'Whisper words of wisdom let it be',

'And when the night is cloudy',
'There is still a light that shines on me',
'Shine on until tomorrow let it be',
'I wake up to the sound of music',
'Mother Mary comes to me',
'Speaking words of wisdom let it be',

'Let it be let it be',
'Let it be yeah let it be',
'Oh there will be an answer let it be',
'Let it be let it be',
'Let it be yeah let it be',
'Whisper words of wisdom let it be']

doc=lyrics
d=dict()
for line in doc:
    words=line.split()
    for word in words:
        if word not in d:
            d[word]=1
        else:
            d[word]+=1
print d
m=list()
for f in d:
    if d[f]>=20:
        m.append(f)
print ""
print "Words that occur more than 20 times is", m
input()