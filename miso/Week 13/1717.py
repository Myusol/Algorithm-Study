import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [x for x in range(n + 1)]

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    parent[rootB] = rootA

def check(a, b):
    if find(a) != find(b):
        return 'NO'
    else:
        return 'YES'

for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union(a, b)
    else:
        if find(a) != find(b):
            print('NO')
        else:
            print('YES')