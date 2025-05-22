import sys
input = sys.stdin.readline
N, M = map(int, input().split())
office = []
cctvs = []
for y in range(N):
    office.append(list(map(int, input().split())))
    for x in range(M):
        if 1 <= office[y][x] <= 5 :
            cctvs.append((x, y, office[y][x])) # cctv 위치와 방향이 저장되어야 함

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cctv_directions = {
    1: [[0], [1], [2], [3]], # 1번: 4방향 중 하나
    2: [[0, 2], [1, 3]],     # 2번: 양쪽 두 방향 (2가지)
    3: [[0, 1], [1, 2], [2, 3], [3, 0]], # 3번: 직각 방향 (4가지)
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], # 4번: 세 방향 (4가지)
    5: [[0, 1, 2, 3]],       # 5번: 네 방향 모두 (1가지)
}

cctvs.sort(key=lambda x: -x[2]) # cctv 번호 기준 내림차순으로 정렬

blindspot = 65 # 사무실 가로, 세로의 최대가 8이기 때문에 크기보다 1크게

def watch(x, y, directions, map):
    for d in directions: # cctv_directions에 들어있는 방향들을 다 탐색해보는 것것
        nx, ny = x, y
        while True: # 범위가 벗어나거나, 벽을 만나기 전까지는 감시가 되는 구역
            nx += dx[d]
            ny += dy[d]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                break
            if map[ny][nx] == 6:
                break
            if map[ny][nx] == 0:
                map[ny][nx] = '#'

def dfs(depth, map):
    global blindspot
    
    if depth == len(cctvs): # 모든 CCTV 선택 완료 -> 사각지대 계산
        cnt = sum(row.count(0) for row in map) # 사각지대인 0을 count
        blindspot = min(blindspot, cnt) # 사각지대가 적은 것으로 갱신
        return
    
    x, y, num = cctvs[depth]
    for directions in cctv_directions[num]: # 각 번호 cctv의 방향 전부 탐색
        tmp_office = [row[:] for row in map] # 각 번호별로 감시구역이 표시가 되어야하므로 deepcopy가 되어야 함
        watch(x, y, directions, tmp_office) # 방향에서 감시되는 구역 표시
        dfs(depth + 1, tmp_office) # 다음 cctv로 넘어감
        
dfs(0, office)
print(blindspot)