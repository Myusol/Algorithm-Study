import sys
from collections import defaultdict

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

cnt = defaultdict(int)
current_unique = 0

for i in range(k):
    if cnt[sushi[i]] == 0:
        current_unique += 1
    cnt[sushi[i]] += 1

max_unique = current_unique + (0 if cnt[c] else 1)

for i in range(1, n):
    remove = sushi[i - 1]
    add = sushi[(i + k - 1) % n]

    cnt[remove] -= 1
    if cnt[remove] == 0:
        current_unique -= 1

    if cnt[add] == 0:
        current_unique += 1
    cnt[add] += 1

    total_unique = current_unique + (0 if cnt[c] else 1)
    max_unique = max(max_unique, total_unique)

print(max_unique)