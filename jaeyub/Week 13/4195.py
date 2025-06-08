import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        number[a] += number[b]
    print(number[a])

T = int(input())

for _ in range(T):
    F = int(input())
    parent, number = {}, {}
    for i in range(F):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)