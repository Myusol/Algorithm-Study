import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())

# 상어 정보 저장
sharks = dict()
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[(r - 1, c - 1)] = [s, d - 1, z]

# 방향: 위, 아래, 오른쪽, 왼쪽
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

result = 0

for t in range(C):  # 낚시왕 이동
    # 1. 낚시왕이 상어를 잡는다
    for i in range(R):
        if (i, t) in sharks:
            result += sharks[(i, t)][2]
            del sharks[(i, t)]
            break

    # 2. 상어 이동
    new_sharks = dict()
    for (r, c), (s, d, z) in sharks.items():
        if d in [0, 1]:  # 세로 방향
            cycle = (R - 1) * 2
            move = s % cycle
            for _ in range(move):
                if r + dr[d] < 0 or r + dr[d] >= R:
                    d = 1 - d  # 위 <-> 아래
                r += dr[d]
        else:  # 가로 방향
            cycle = (C - 1) * 2
            move = s % cycle
            for _ in range(move):
                if c + dc[d] < 0 or c + dc[d] >= C:
                    d = 5 - d  # 왼 <-> 오 (3 <-> 2)
                c += dc[d]

        # 상어 충돌 처리
        if (r, c) in new_sharks:
            if new_sharks[(r, c)][2] < z:
                new_sharks[(r, c)] = [s, d, z]
        else:
            new_sharks[(r, c)] = [s, d, z]

    sharks = new_sharks

print(result)