# 도영이가 만든 맛있는 음식 / 실버2
import sys
# 모든 가능한 조합을 자동으로 만들어주는 함수
from itertools import combinations
input = sys.stdin.readline
n = int(input())
sour = []
bitter = []
for _ in range(n):
    a, b = map(int, input().split())
    sour.append(a)
    bitter.append(b)
diff = float('inf')
for i in range(1, n + 1):
    for food in combinations(range(n), i):
        s = 1
        b = 0
        for j in food:
            s *= sour[j]
            b += bitter[j]
        diff = min(diff, abs(s - b))
print(diff)