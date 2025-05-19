import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
house = []
chicken = []
for i in range(N):
    city = list(map(int, input().split()))
    for j in range(N):
        if city[j] == 1:
            house.append((i, j))
        elif city[j] == 2:
            chicken.append((i, j))

mindist = 1e6

for chickens in combinations(chicken, M):
    totaldist = 0
    for hy, hx in house:
        dist = min(abs(hy - cy) + abs(hx - cx) for cy, cx in chickens)
        totaldist += dist
    mindist = min(mindist, totaldist)
    
print(mindist)