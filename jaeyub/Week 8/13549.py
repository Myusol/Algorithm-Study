from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
time = [0] * 100001

deq = deque()
deq.append(N)

while deq:
    x = deq.popleft()
    if x == K:
        print(time[x])
        break

    for y in (x*2, x-1, x+1):
        if 0 <= y <= 100000 and not time[y]:
            if y == x*2:
                time[y] = time[x]
            else:
                time[y] = time[x] + 1
            deq.append(y)