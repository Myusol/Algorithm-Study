import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
parent = [x for x in range(N + 1)]
A = [0] + list(map(int, input().split()))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if A[x] < A[y]:
        parent[y] = x
    else:
        parent[x] = y

for _ in range(M):
    x, y = map(int, input().split())
    union(x, y)

result = 0
for i in range(1, N + 1):
    if i == find(i):
        result += A[i]
if K >= result:
    print(result)
else:
    print("Oh no")