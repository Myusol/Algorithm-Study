import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 1
cnt = 0
current_sum = arr[0]

while end <= N:
    while current_sum >= M:
        if current_sum == M:
            cnt += 1
        current_sum -= arr[start]
        start += 1
    if end < N:
        current_sum += arr[end]
    end += 1

print(cnt)