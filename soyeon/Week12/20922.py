import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

cnt = [0] * 100001
left = 0
max_len = 0

for right in range(n):
    cnt[nums[right]] += 1

    while cnt[nums[right]] > k:
        cnt[nums[left]] -= 1
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)