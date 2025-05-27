# 집합의 표현 / 골드5
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def find(x):
    if parent[x] != x: # 자기 자신이 대표가 아닐 시
        parent[x] = find(parent[x]) # 경로 압축(x를 호출하는 순간, x의 부모를 바로 루트로 바꿈)
    return parent[x]
def union(a,b): # a, b의 루트를 찾아서 같은 집합으로 합침
    root1 = find(a)
    root2 = find(b)
    if root1 != root2: # 루트가 다르면 b의 루트를 a의 루트에 붙임
        parent[root2] = root1
n, m = map(int, input().split())
# 우선 독립으로 만들기
parent = [i for i in range(n+1)]
for _ in range(m):
    cmd, a, b = map(int,input().split())
    if cmd == 0:
        union(a,b) # a, b 집합을 합침
    elif cmd == 1:
        print('YES' if find(a) == find(b) else 'NO') # 같은 집합인지아닌지 확인