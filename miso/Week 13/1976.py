import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
parent = [i for i in range(N)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if find(x) != find(y):
        parent[find(y)] = find(x)

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            union(i, j)

plan = list(map(int, input().split()))
plan = [i - 1 for i in plan]

root = find(plan[0])

for city in plan:
    if find(city) != root:
        print('NO')
        break
else:
    print('YES')