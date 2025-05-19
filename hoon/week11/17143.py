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
        j,k,s,d,z = shark.pop()
        for _ in range(s): # 상어 속력만큼 한칸씩 이동
            j = j+dx[d-1] # d(방향)에 맞춰서 상어의 위치를 이동
            k = k+dy[d-1]
            if k<0 or j<0 or j>R-1 or k>C-1: # 범위 지정
                if d==1: # 위로 이동이면 아래로
                    d=2
                elif d==2: # 아래로 가면 위로
                    d=1
                elif d==3: # 오른쪽으로 가면 왼쪽으로
                    d=4
                elif d==4: # 왼쪽으로 가면 오른쪽으로
                    d=3
                # 위에서 방향 바꾼거 다시 적용
                j = j+dx[d-1]
                k = k+dy[d-1] 
                j = j+dx[d-1]
                k = k+dy[d-1] 
        pan[j][k].append([s,d,z]) # 다시 정보 저장
    # 같은 자리에 있는 상어 잡아먹기
    for j in range(R):
        for k in range(C):
            if len(pan[j][k])>=2: # 2마리 이상이면
                pan[j][k].sort(key=lambda x:-x[2]) # = x[2], reverse=True
                # [s,d,z] 이렇게 저장 했으니까 2번째 열 기준으로 정렬해서 하나 남을때까지 제거(-x 기때문에 음수로 바뀌니까 내림 차순으로 바뀜)
                while len(pan[j][k])>1:
                    pan[j][k].pop()
print(result)