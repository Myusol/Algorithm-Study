# 색종이 만들기 / 실버2
import sys
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 각 줄마다 받아서 저장
result = []
# x, y 현재 영역의 시작 좌표, N 현재 영역의 한 변의 길이
def squ(x, y, N):
    # 현재 영역의 시작 위치의 색을 저장 (0, 1)(그걸 기준으로 다 같은지 보는거임)
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            # 만약 시작 색과 다른 색이 하나라도 발견되면 영역을 4등분함
            if color != paper[i][j]:
                # 왼쪽 위 영역 분할 (시작 좌표: (x, y))
                squ(x, y, N//2)
                # 오른쪽 위 영역 분할 (시작 좌표: (x, y+N//2))
                squ(x, y+N//2, N//2)
                # 왼쪽 아래 영역 분할 (시작 좌표: (x+N//2, y))
                squ(x+N//2, y, N//2)
                # 오른쪽 아래 영역 분할 (시작 좌표: (x+N//2, y+N//2))
                squ(x+N//2, y+N//2, N//2)
                return # 함수 전체 종료
    # 현재 영역 내의 모든 칸이 같은 색일때
    if color == 0: # 0이면 0추가
        result.append(0)
    else: # 1이면 1추가
        result.append(1)
squ(0, 0, N)
print(result.count(0)) # 0개수 출력
print(result.count(1)) # 1개수 출력