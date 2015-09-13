import re
from collections import defaultdict

def _make_equal_length(a):
    return '0'*(4-len(str(a))) + str(a)
chi={}
with open("chiq7.csv","r") as f:
    content = f.readlines()
    for x in content:
        
        lis=x.split(",")

        chi[lis[0]]=lis[1]

val1=sorted(chi, key=lambda key: chi[key])
print 'sorted order is:'
for content in val1:
    
    print 'VAR_'+_make_equal_length(int(chi[content]))
    

''' NOte:
index 1934 --> target in train.csv
1 ->ID
2-----1932 -->VAR's missing: 218, 240'''
