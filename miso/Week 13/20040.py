import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [x for x in range(n)]

def find(x) :
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