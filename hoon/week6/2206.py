# 벽 부수고 이동하기 / 골드3
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
maze = [list(map(int,input().strip())) for _ in range(n)] 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    queue = deque()
    queue.append((0, 0, 0)) # 출발 위치,벽을 부쉈는지 여부
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] # 3차원 배열로 만듬 *2는 0, 1 이라서
    visited[0][0][0] = 1 # 처음엔 벽을 안부순 상태이며 한걸음 포함해서 1로 시작
    while queue:
        x,y,f = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 건너갈 칸이 0이고 벽 부수기 안한 경우
            if maze[nx][ny] == 0 and visited[nx][ny][f] == 0:
                visited[nx][ny][f] = visited[x][y][f] + 1 
                queue.append((nx, ny, f))
            # 건너갈 칸이 1이고 벽부순적 없고 벽을 부수고 이 칸을 온적이 없을 경우
            elif maze[nx][ny] == 1 and f == 0 and visited[nx][ny][1] == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1 # f를 1로 바꿈 그리고 스탭+1
                queue.append((nx, ny, 1))

    end_not_f = visited[n-1][m-1][0] # 벽 안 부수고 도착 스탭
    end_f = visited[n-1][m-1][1] # 벽 한번 부수고 도착 스탭
    # 둘다 도착한 경우
    if end_not_f and end_f: # 0,None,'',[],False가 아니면 실행 즉, 참이면 실행
        return min(end_not_f, end_f)
    elif end_not_f:
        return end_not_f
    elif end_f:
        return end_f
    else:
        return -1
print(bfs())