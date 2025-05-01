import sys
import bisect

input = sys.stdin.readline

n, h = map(int, input().split())

bottom = []
top = []

for i in range(n):
    x = int(input())
    if i % 2 == 0:
        bottom.append(x)
    else:
        top.append(x)

bottom.sort()
top.sort()

min_crash = n + 1
cnt = 0

for height in range(1, h + 1):
    bottom_crash = len(bottom) - bisect.bisect_left(bottom, height)
    top_crash = len(top) - bisect.bisect_left(top, h - height + 1)

    total = bottom_crash + top_crash

    if total < min_crash:
        min_crash = total
        cnt = 1
    elif total == min_crash:
        cnt += 1

print(min_crash, cnt)