n, m = map(int, input().split())
lectures = list(map(int, input().split()))

lo = max(lectures)
hi = sum(lectures)
answer = hi

while lo <= hi:
    mid = (lo + hi) // 2
    cnt = 1
    total = 0

    for length in lectures:
        if total + length > mid:
            cnt += 1
            total = length
        else:
            total += length

    if cnt <= m:
        answer = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(answer)
