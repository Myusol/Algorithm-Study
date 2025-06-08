import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if A[a] < A[b]:
        parent[b] = a
    else:
        parent[a] = b

N, M, K = map(int, input().split())
parent = [x for x in range(N+1)]
A = [0] + list(map(int, input().split()))

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

ans = 0
for i in range(1, N+1):
    if i == find(i):
        ans += A[i]
if K >= ans:
    print(ans)
else:
    print("Oh no")