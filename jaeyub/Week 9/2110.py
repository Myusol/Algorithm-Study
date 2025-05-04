import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

start, end = 1, house[-1] - house[0]
answer = 0

while start <= end :
    mid = (start + end) // 2
    prev, cnt = house[0], 1
    for i in range(1, N) :
        if house[i] - prev >= mid :
            cnt += 1
            prev = house[i]
    if cnt >= C :
        answer = max(answer, mid)
        start = mid + 1
    else :
        end = mid - 1

print(answer)