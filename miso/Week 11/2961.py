import sys
from itertools import combinations 
input = sys.stdin.readline
N = int(input())

ingredient = []
for i in range(N):
    s, b = map(int, input().split())
    ingredient.append((s, b))

diff = 1e9
for i in range(N):
    for food in combinations(ingredient, i + 1):
        sour, bitter = 1, 0
        for s, b in food:
            sour *= s
            bitter += b
        diff = min(diff, abs(sour - bitter))

print(diff)