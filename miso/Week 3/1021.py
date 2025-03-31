from collections import deque
import sys
n,m=map(int,sys.stdin.readline().split())
npop=list(map(int,sys.stdin.readline().split()))
deq=deque([])
cnt=0
for i in range(n):
    deq.append(i+1)
for i in range(m):
    if deq.index(npop[i])==0:
            deq.popleft()
    else:
        if deq.index(npop[i])<=len(deq)//2:
            while deq.index(npop[i])!=0:
                deq.rotate(-1)
                cnt+=1
            deq.popleft()
        else:
            while deq.index(npop[i])!=0:
                deq.rotate(1)
                cnt+=1
            deq.popleft()
print(cnt)


########

from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
npop = list(map(int, sys.stdin.readline().split()))
deq = deque(range(1, n + 1))
cnt = 0
for i in npop:
    idx = deq.index(i)
    if idx <= len(deq) // 2:
        while deq[0] != i:
            deq.rotate(-1)
            cnt += 1
    else:
        while deq[0] != i:
            deq.rotate(1)
            cnt += 1
    deq.popleft()
print(cnt)
