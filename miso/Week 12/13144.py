import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
num = set()

start, end, cnt = 0, 0, 0
while start < N and end < N:
    num.add(arr[end])
    if end - start + 1 == len(num):
        cnt += end - start + 1
        end += 1
    else:
        num.remove(arr[start])
        start += 1
print(cnt)