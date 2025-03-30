import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
max_score = arr
min_score = arr
for _ in range(N - 1):
    arr = list(map(int, sys.stdin.readline().split()))
    max_score = [arr[0] + max(max_score[0], max_score[1]), arr[1] + max(max_score), arr[2] + max(max_score[1], max_score[2])]
    min_score = [arr[0] + min(min_score[0], min_score[1]), arr[1] + min(min_score), arr[2] + min(min_score[1], min_score[2])]

print(max(max_score), min(min_score))