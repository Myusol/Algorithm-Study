import sys
input = sys.stdin.readline
N, C = map(int, input().split())
wifi = sorted(int(input()) for _ in range(N))

def router(d):
    cnt = 1
    r = wifi[0]
    
    for i in range(1, N):
        if wifi[i] - r >= d:
            cnt += 1
            r = wifi[i]
    return cnt
            
s, e = 1, wifi[-1] - wifi[0]
dist = 0

while s <= e:
    m = (s + e) // 2
    
    if router(m) >= C:
        dist = m
        s = m + 1
    else:
        e = m - 1

print(dist)