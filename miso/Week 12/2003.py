import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

start, end, cnt = 0, 0, 0
total = A[0]
while end <= N - 1:
    if total >= M:
        if total == M:
            cnt += 1
        total -= A[start]
        start += 1
    elif end < N - 1:
        end += 1
        total += A[end]
    else:
        break
    
print(cnt)