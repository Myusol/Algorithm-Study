import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)
T = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if find(x) != find(y):
        parent[find(y)] = find(x)
        number[find(x)] += number[find(y)]
    print(number[find(x)])

for _ in range(T):
    F = int(input())
    parent, number = {}, {}
    for i in range(F):
        x, y = input().split()
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        union(x, y)