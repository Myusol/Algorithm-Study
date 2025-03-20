import sys
from collections import defaultdict
n,c=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
dict=defaultdict(int)
for i in arr:
    dict[i]+=1
sort_dict=sorted(dict.items(),key=lambda x:x[1],reverse=True)
print(*[(str(i[0])+' ')*i[1] for i in sort_dict],sep='')

#######

import sys
n,c=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
dict={}
for i in arr:
    dict[i]=dict.get(i,0)+1
sort_dict=sorted(dict.items(),key=lambda x:x[1],reverse=True)
print(*[(str(i[0])+' ')*i[1] for i in sort_dict],sep='')

#######

import sys
from collections import Counter
n,c=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
for key,value in Counter(arr).most_common():
    for _ in range(value):
        print(key, end=' ')