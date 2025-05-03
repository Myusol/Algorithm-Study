N, K = int(input()), int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2
    
    find = 0
    for i in range(1, N+1):
        find += min(mid//i, N)
    
    if find >= K:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
