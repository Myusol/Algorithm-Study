# 스타트링크 / 실버1
# f = 층수 s = 현위치 g = 도착지 u = 위로 d = 아래로
from collections import deque
import sys
input = sys.stdin.readline
f, s, g, u, d = map(int,input().split())
check = [-1 for _ in range(f+1)] # -1 로 초기화해서 방문 여부 확인
def bfs():
    queue = deque()
    queue.append(s)
    check[s] = 0 # 시작 지점 방문 처리
    while queue:
        y = queue.popleft() # 현재 위치
        if y == g: # 현재 위치랑 목표 위치가 같다면
            return check[y] # 버튼 누릇 횟수 반환
        else: #      1+2 부터 1-1까지
            for x in (y + u, y - d): # 위로 u층, 아래로 d층 각각 하나씩 시도
                    # 범위 체크 및 미방문 확인
                if (0 < x <= f) and check[x] == 0:
                    check[x] = check[y] + 1
                    queue.append(x)
    return 'use the stairs'
print(bfs())