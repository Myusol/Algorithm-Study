import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))

window_sum = sum(temp[:k])
max_sum = window_sum

for i in range(k, n):
    window_sum = window_sum - temp[i-k] + temp[i]
    max_sum = max(max_sum, window_sum)

print(max_sum)