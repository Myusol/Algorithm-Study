import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
parent = [i for i in range(G + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)

cnt = 0
for _ in range(P):
    gi = int(input())
    docking = find(gi)
    if docking == 0:
        break
    cnt += 1
    union(docking, docking - 1)
print(cnt)