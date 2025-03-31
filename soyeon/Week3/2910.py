import sys
from collections import Counter

n, c = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

counter = Counter(nums)
order = {}

for idx, num in enumerate(nums):
    if num not in order:
        order[num] = idx

sorted_nums = sorted(counter.keys(), key=lambda x: (-counter[x], order[x]))

result = []
for num in sorted_nums:
    result.extend([num] * counter[num])

print(*result)