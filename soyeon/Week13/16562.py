import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, K = map(int, input().split())
money = [0] + list(map(int, input().split()))  # 인덱스 맞추기 위해 앞에 0 추가
parent = [i for i in range(N+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return
    # 친구비가 더 적은 쪽을 부모로
    if money[root_a] < money[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

group_min_cost = set()
for i in range(1, N+1):
    group_min_cost.add(find(i))  # 대표 노드 모음

total_cost = 0
used = set()
for root in group_min_cost:
    if root not in used:
        total_cost += money[root]
        used.add(root)

if total_cost <= K:
    print(total_cost)
else:
    print("Oh no")