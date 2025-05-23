import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))

start, end = 0, 0
ans = 1e9
sum = 0

while True :
    if sum >= S :
        ans = min(ans, end - start)
        sum -= num[start]
        start += 1
    else :
        if end == N :
            break
        sum += num[end]
        end += 1

if ans == 1e9 :
    print(0)
else :
    print(ans)