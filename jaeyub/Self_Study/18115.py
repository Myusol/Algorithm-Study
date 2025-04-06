from collections import deque
import sys

N = int(sys.stdin.readline())
dq = deque()

cmd = list(map(int,sys.stdin.readline().split()))
cmd.reverse()

num=0
for c in cmd:
    num+=1
    if c ==1:
        dq.appendleft(num)
    elif c==2:
        dq.insert(1,num)
    else:
        dq.append(num)
li = list(dq)
print(*li)