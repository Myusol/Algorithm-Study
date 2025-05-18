# 낚시왕 / 골드1 / 개선 버전
# 낚시왕 / 골드1
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
        nj, nk, nd = j, k, d
        if d == 1 or d == 2:  # 위 아래로 움직이는 상어는
            move = s % ((R-1)*2) # 세
            for _ in range(move):
                if nd == 1 and nj == 0: # 위쪽 끝에 도달하면 방향 아래로
                    nd = 2
                elif nd == 2 and nj == R-1: # 아래 끝 도달하면 위로
                    nd = 1
                nj += dx[nd-1] # 한칸 이동
        else:  # 그외 즉 오른쪽 왼쪽
            move = s % ((C-1)*2)
            for _ in range(move):
                if nd == 4 and nk == 0: # 왼쪽 끝에 도달하면 오른쪽
                    nd = 3
                elif nd == 3 and nk == C-1: # 오른쪽 끝에 도달하면 왼쪽
                    nd = 4
                nk += dy[nd-1]
        pan[nj][nk].append([s, nd, z]) # 다시 원래대로 저장


    # 같은 자리에 있는 상어 잡아먹기
    for j in range(R):
        for k in range(C):
            if len(pan[j][k])>=2: # 2마리 이상이면
                pan[j][k].sort(key=lambda x:-x[2]) # = x[2], reverse=True
                # [s,d,z] 이렇게 저장 했으니까 2번째 열 기준으로 정렬해서 하나 남을때까지 제거(-x 기때문에 음수로 바뀌니까 내림 차순으로 바뀜)
                while len(pan[j][k])>1:
                    pan[j][k].pop()
print(result)