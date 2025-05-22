import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
total = arr[0]
result = N + 1
while True:
    if total >= S:
        result = min(result, end - start + 1)
        total -= arr[start]
        start += 1
    elif end < N - 1:
        end += 1
        total += arr[end]
    else:
        break
        
print(result if result != N + 1 else 0)