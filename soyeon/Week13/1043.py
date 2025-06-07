import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if a < b:
        parent[b] = a
    else:
        parent[a] = b    

N, M = list(map(int, input().split()))
parent = [i for i in range(N + 1)]
truth = list(map(int, input().split()))[1:]

know_truth = 0
for person in truth:
    parent[person] = know_truth

parties = []
for i in range(M):
    party = list(map(int, input().split()))[1:]
    for i in range(len(party) - 1):
        union(party[i], party[i + 1])
    parties.append(party)

answer = 0

for party in parties:
    know = False
    for i in range(len(party)):
        if find(party[i]) == know_truth:
            know = True
            break
    if not know:
        answer += 1

print(answer)