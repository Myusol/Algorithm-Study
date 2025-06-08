import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]
true = list(map(int, input().split()))
p_list = [list(map(int, input().split())) for _ in range(m)]

def find(x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    x = find(a)
    y = find(b)
    parent[y] = x

if true[0] == 0:
    print(m)
    exit()

for i in range(2, len(true)):
    union(true[1], true[i])

for party in p_list:
    for i in range(2, len(party)):
        union(party[1], party[i])

answer = 0
x = find(true[1])

for party in p_list:
    if find(party[1]) != x:
        answer += 1

print(answer)