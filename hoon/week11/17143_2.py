# 낚시왕 / 골드1 / 개선 버전
import sys
input = sys.stdin.readline
R,C,M = map(int, sys.stdin.readline().split()) # 세로 가로 상어의 수
if M == 0:
    print(0)
    sys.exit()
sharkinfo = [list(map(int, input().split())) for _ in range(M)]
pan = [[[] for i in range(C)] for _ in range(R)]
shark = []
#  (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기
# d(이동)는 1~4 위 아래 오른쪽 왼쪽
while sharkinfo:
    r,c,s,d,z = sharkinfo.pop()
    pan[r-1][c-1].append([s,d,z])
result = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]
# 낚시왕 이동
for i in range(C): # 격자판 가로 만큼 반복
    # 땅과 가장 가까운 상어 잡기
    for j in range(R):
        if pan[j][i]:
            s,d,z = pan[j][i].pop()
            result += z
            break # 위에서 부터 확인 하니까 가까운거 먼저 잡게 됨
    # 상어 이동
    for j in range(R):
        for k in range(C):
            if pan[j][k]:
                s,d,z=pan[j][k].pop()
                shark.append([j,k,s,d,z]) # pan에 있던 상어 정보를 shark 리스트에 임시로 저장
    while shark:
        j, k, s, d, z = shark.pop()
        if d == 1 or d == 2:  # 위/아래 이동
            cycle = (R-1)*2
            move = s % cycle
            if d == 1:  # 위로 이동
                if move <= j:
                    nj = j - move
                    nd = 1
                else:
                    move -= j
                    if move <= R-1:
                        nj = move
                        nd = 2
                    else:
                        nj = 2*(R-1) - move
                        nd = 1
            else:  # 아래로 이동
                if move <= R-1-j:
                    nj = j + move
                    nd = 2
                else:
                    move -= (R-1-j)
                    if move <= R-1:
                        nj = R-1 - move
                        nd = 1
                    else:
                        nj = move - (R-1)
                        nd = 2
            nk = k
        else:  # 오른쪽/왼쪽 이동
            cycle = (C-1)*2
            move = s % cycle
            if d == 4:  # 왼쪽
                if move <= k:
                    nk = k - move
                    nd = 4
                else:
                    move -= k
                    if move <= C-1:
                        nk = move
                        nd = 3
                    else:
                        nk = 2*(C-1) - move
                        nd = 4
            else:  # 오른쪽
                if move <= C-1-k:
                    nk = k + move
                    nd = 3
                else:
                    move -= (C-1-k)
                    if move <= C-1:
                        nk = C-1 - move
                        nd = 4
                    else:
                        nk = move - (C-1)
                        nd = 3
            nj = j
        pan[nj][nk].append([s, nd, z])
    # 같은 자리에 있는 상어 잡아먹기
    for j in range(R):
        for k in range(C):
            if len(pan[j][k])>=2: # 2마리 이상이면
                pan[j][k].sort(key=lambda x:-x[2]) # = x[2], reverse=True
                # [s,d,z] 이렇게 저장 했으니까 2번째 열 기준으로 정렬해서 하나 남을때까지 제거(-x 기때문에 음수로 바뀌니까 내림 차순으로 바뀜)
                while len(pan[j][k])>1:
                    pan[j][k].pop()
print(result)