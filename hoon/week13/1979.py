# 여행 가자 / 골드4
import sys
input = sys.stdin.readline
n = int(input()) # 도시 수
m = int(input()) # 여행 계획 속 도시 수
parent = [i for i in range(n)]
def find(x):
    if parent[x] != x: # 자기 자신이 대표가 아닐 시
        parent[x] = find(parent[x]) # 경로 압축(x를 호출하는 순간, x의 부모를 바로 루트로 바꿈)
    return parent[x]
def union(a,b): # a, b의 루트를 찾아서 같은 집합으로 합침
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            union(i, j)
plan = list(map(int, input().split()))
plan = [i- 1 for i in plan] # 0부터 시작 하도도록 만들기
root = find(plan[0])
for city in plan:
    if find(city) != root:
        print('NO')
        break
else:
    print('YES')