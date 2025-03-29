# 하노이 탑 이동 순서/ 골드5
# start=시작, end= 끝 aux=중간장대 moves=이동경로
import sys
input = sys.stdin.readline
n = int(input())
def hano(n, start, end, aux, moves):
    if n==1: # n이 1이면 바로 이동
        moves.append((start,end))
    else:
        hano(n-1,start,aux,end,moves) # n-1개 원판을 보조로 이동
        moves.append((start,end)) # 가장 큰 원판을 도착지로 이동
        hano(n-1,aux,end,start,moves) # 보조 장대에서 n-1개 원판을 이동
moves = [] # 이동경로 저장
hano(n,1,3,2,moves)
print(len(moves)) # 총 이동 횟수
for move in moves: # 이동을 어디서 어디로 이동했는지 출력
    print(move[0],move[1])