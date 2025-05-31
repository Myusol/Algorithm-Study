import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
true = list(map(int, input().split()))
p_list = [list(map(int, input().split())) for _ in range(M)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(y)] = find(x)

if true[0] == 0:
    print(M)
    exit()

for i in range(2, len(true)):
    union(true[1], true[i])

for party in p_list:
    for i in range(2, len(party)):
        union(party[1], party[i])

answer = 0
x = find(true[1])

for party in p_list:
    if all(find(person) != x for person in party[1:]):
        answer += 1

print(answer)