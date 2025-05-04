n = int(input())
k = int(input())
start, end = 1, k
ans = 0

while(start <= end):
    mid = (start + end) // 2
    cnt = 0

    for i in range (1, n+1) :
        cnt += min(n, mid // i)
        
    if cnt >= k:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)