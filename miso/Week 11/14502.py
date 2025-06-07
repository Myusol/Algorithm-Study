import sys
from collections import deque
from itertools import combinations 
input = sys.stdin.readline
N, M = map(int, input().split())
lab = []
virus = []
safe = 0
for y in range(N):
    lab.append(list(map(int, input().split())))
    for x in range(M):
        if lab[y][x] == 2: # 바이러스라면 좌표를 리스트에 추가
            virus.append((x, y))

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(tmp_lab): # bfs를 활용하여 바이러스를 끝까지 퍼뜨림
    q = deque(virus) # 모든 상황에서 바이러스를 퍼뜨려 봐야하기 때문에 q에 복사 후 사용
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if tmp_lab[ny][nx] == 0:
                    tmp_lab[ny][nx] = 2
                    q.append((nx, ny))
                    
    return sum(row.count(0) for row in tmp_lab) # 안전 구역 개수를 return

def wall():
    global safe
    empty = [(i, j) for j in range(N) for i in range(M) if lab[j][i] == 0] # 벽을 설치 할 수 있는 곳을 empty 리스트에 저장
    
    for walls in combinations(empty, 3): # combinations 함수를 활용하여 벽 3개를 설치할 수 있는 조합을 walls에 만듦
        tmp_lab = [row[:] for row in lab]
        
        for x, y in walls: # 선택된 3개 좌표에 벽을 설치
            tmp_lab[y][x] = 1
            
        safe = max(safe, bfs(tmp_lab)) # 벽이 설치된 연구실을 기준으로 바이러스를 확산시킨 후 안전 구역 갱신

    print(safe)
    
wall()