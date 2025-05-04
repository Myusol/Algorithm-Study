# 개똥벌레 / 골드5
import sys
import bisect
input = sys.stdin.readline
N, H = map(int,input().split())
down = []
up = []
for i in range(N):
    a = int(input())
    if i % 2 == 0:
        down.append(a)
    else:
        up.append(a)
down.sort()
up.sort()
count = 0
for i in range(1, H + 1):
    # bisect 는 bisect_left라는 함수를 쓰면 i와 같거나 이상 처음 위치를 반환
    # i랑 크거나 같은 첫 위치를 찾고 그 뒤는 전부 충돌함
    down_c = len(down) - bisect.bisect_left(down, i)
    # 위에서 부터 크기가 내려오니까 동굴 높이에서 개똥벌레높이를 빼면 종유석 충돌 개수 계산
    up_c = len(up) - bisect.bisect_left(up, H - i + 1)
    total = down_c + up_c
    if total == N:
        count+=1
    elif total < N:
        N = total
        count = 1
print(N, count)