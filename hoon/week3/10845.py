# 큐 / 실버4
import sys
from collections import deque
que = deque()
input = sys.stdin.readline
a = int(input())
result = []
for _ in range(a):
    b = input().split()
    if len(b) == 2:
        s, num = b[0], b[1]
    else:
        s = b[0]
    
    if s == 'push':
        que.append(num)
    elif s == 'pop':
        if len(que) > 0:
            result.append(que[0])
            que.popleft()
        else:
            result.append(-1)
    elif s == 'size': 
        result.append(len(que))
    elif s == 'empty':
        if len(que) == 0:
            result.append(1)
        else:
            result.append(0)
    elif s == 'front':
        if len(que) == 0:
            result.append(-1)
        else:
            result.append(que[0])
    elif s == 'back':
        if len(que) == 0:
            result.append(-1)
        else:
            result.append(que[-1])
sys.stdout.write('\n'.join(map(str,result)))