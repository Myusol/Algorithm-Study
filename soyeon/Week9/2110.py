import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n) :
    house.append(int(input()))
house.sort()

start, end = 1, max(house) - min (house)
ans = 0

while start <= end :
    mid = (start + end) // 2
    set = house[0]
    cnt = 1

    for i in house :
        if (i - set >= mid) :
            cnt += 1
            set = i

    if cnt >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
print(ans)