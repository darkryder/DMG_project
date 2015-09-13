import re
from collections import defaultdict

f1=open('ansq6.csv','a+')
def _make_equal_length(a):
    return '0'*(4-len(str(a))) + str(a)
gain={}
with open("gain.csv","r") as f:
    content = f.readlines()
    for x in content:
        
        lis=x.split(",")

        gain[(lis[1].split("\n"))[0]]=lis[0] #key should be gain value and value should be attribute value

val1=sorted(gain.iteritems(), key=lambda (x,y):float(x))#sort on key basis/gain basis
print val1
print 'sorted order is:'
for content in range(0,len(val1)): #displays rank (value based-->var name)
    
    data='VAR_'+_make_equal_length(int(val1[content][1]))#print attr [0] from csv
    print data
    f1.write(data+str('\n'))#ans write to file
    
f1.close()
