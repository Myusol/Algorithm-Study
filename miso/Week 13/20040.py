# 랭크기반 병합
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [x for x in range(n)]
rank = [0] * n

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX == rootY:
        return True
    
    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    else:
        parent[rootY] = rootX
        if rank[rootX] == rank[rootY]:
            rank[rootX] += 1
    return False
    
for i in range(1, m + 1):
    a, b = map(int, input().split())
    if union(a, b):
        print(i)
        break
else:
    print(0)

# 단순 min, max 기준
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [x for x in range(n)]

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    x, y = min(x, y), max(x, y)
    rootX = find(x)
    rootY = find(y)
    if rootX == rootY:
        return True
    parent[rootY] = rootX
    return False
    
for i in range(1, m + 1):
    a, b = map(int, input().split())
    if union(a, b):
        print(i)
        break
else:
    print(0)