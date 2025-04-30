import sys
input = sys.stdin.readline

def count_obs(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    return len(arr) - start

N, H = map(int, input().split())
bottom, top = [], []

for i in range(N):
    h = int(input())
    if i % 2 == 0:
        bottom.append(h)
    else:
        top.append(h)

bottom.sort()
top.sort()

min_obs = N
count = 0

for i in range(1, H + 1):
    b = count_obs(bottom, i)
    t = count_obs(top, H - i + 1)
    total = b + t

    if total < min_obs:
        min_obs = total
        count = 1
    elif total == min_obs:
        count += 1

print(min_obs, count)
