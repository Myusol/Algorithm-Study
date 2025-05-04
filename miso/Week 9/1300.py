import sys
input = sys.stdin.readline
N = int(input())
k = int(input())

s, e = 1, k
val = 0

while s <= e:
    m = (s + e) // 2
    cnt = 0
    
    for i in range(1, N + 1):
        cnt += min(N, m // i)
        
    if cnt < k:
        s = m + 1
    else:
        val = m
        e = m - 1

print(val)