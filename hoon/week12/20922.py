# 겹치는 건 싫어 / 실버1
import sys
from collections import defaultdict
input = sys.stdin.readline
n, k = map(int,input().split())
arr = list(map(int, input().split()))
count = defaultdict(int) # 존재 하지 않는 키 접근 시 자동으로 0 반환
left = 0
max_len = 0
for right in range(n):
    count[arr[right]] += 1
    while count[arr[right]] > k: # k번을 초과하면 left를 1증가 그리고 빠졌으니 카운트는 -1
        count[arr[left]] -= 1
        left += 1
    max_len = max(max_len, right - left + 1) # 최대값 계산하고 갱신
print(max_len)