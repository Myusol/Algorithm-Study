# 이분탐색
import sys
input = sys.stdin.readline
N, H = map(int, input().split())
down, up = [], []
obstacle = [0] * H
for i in range(N):
    if i % 2 == 0:
        down.append(int(input()))
    else:
        up.append(int(input()))
        
def cnt(arr, h):
    s, e = 0, len(arr) - 1
    
    while s <= e:
        m = (s + e) // 2
        if arr[m] < h:
            s = m + 1
        else:
            e = m - 1
    return len(arr) - s

up.sort()
down.sort()

for i in range(H):
    obstacle[i] = cnt(down, i + 1) + cnt(up, H - i)

print(min(obstacle), obstacle.count(min(obstacle)))
    
# 브루트포스
import sys
input = sys.stdin.readline
N, H = map(int, input().split())
obstacle = []
for _ in range(N):
    obstacle.append(int(input()))
    
so = []

for n in range(1, H + 1):
    cnt = 0
    for m in range(N):
        if m % 2 == 0:
            if n <= obstacle[m]:
                cnt += 1
        else:
            if H - n + 1 <= obstacle[m]:
                cnt += 1
    so.append(cnt)
print(min(so), so.count(min(so)))