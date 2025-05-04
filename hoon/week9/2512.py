# 예산 / 실버2
import sys
input = sys.stdin.readline
N = int(input())
requests = list(map(int,input().split()))
M = int(input())
def find(requests, M):
    l, r = 0, max(requests)
    answer = 0
    while l <= r:
        mid = (l + r) // 2
        total = sum(min(r, mid) for r in requests)
        if total <= M:
            answer = mid
            l = mid + 1
        else:
            r = mid - 1
    return answer
print(find(requests, M))