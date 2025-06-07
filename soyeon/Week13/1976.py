import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
M = int(input())
parent = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i

def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for y in range(1, N+1):
    maps = list(map(int, input().split()))
    for x in range(1, len(maps)+1):
        if maps[x-1] == 1:
            union(y, x)

tour = list(map(int, input().split()))
result = set([find(i) for i in tour])
if len(result) != 1:
    print('NO')
else:
    print('YES')