# 연결 요소의 개수 / 실버2
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n + 1)] # graph[1], graph[2] 이런식으로 들어감 (n 최대 숫자까지)
visited = [False] * (n + 1) # False는 방문 X True로 바뀌면 방문 O
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start):
    stack = [start] # 함수 호출시 받는 값을 스택에 넣고 함수 시작
    visited[start] = True # 방문 표시

    while stack:
        node = stack.pop()
        for n in graph[node]: # 꺼낸 함수의 이웃 노드를 전부 파악
            if not visited[n]: # 방문 하지 않은 노드면
                visited[n] = True # 방문으로 바꾸고
                stack.append(n) # stack에 집어 넣어서 다시 반복하게 만들거임

count = 0
for i in range(1, n+1):
    if not visited[i]: # 방문을 안 했으면
        dfs(i) # 함수 실행
        count += 1 # 연결요소 추가
print(count)