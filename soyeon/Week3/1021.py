from collections import deque

N, M = map(int, input().split())
pos = list(map(int, input().split()))
dq = deque(range(1, N+1))

cnt = 0

for p in pos:
    idx = dq.index(p)
    if idx <= len(dq) // 2:
        dq.rotate(-idx)
        cnt += idx
    else:
        dq.rotate(len(dq) - idx)
        cnt += len(dq) - idx
    dq.popleft()

print(cnt)