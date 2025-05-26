# defaultdict를 활용해 count
import sys
from collections import defaultdict
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

eat = defaultdict(int)
window = 0
for i in range(k): # 첫 슬라이딩 윈도우 범위 개수 탐색
    eat[sushi[i]] += 1
    if eat[sushi[i]] == 1: # 초밥 값이 1인 경우라면,
        window += 1 # 새로운 종류의 초밥을 먹은 것이므로 +1

cnt = window
for i in range(N): # 슬라이딩 윈도우를 한칸씩 뒤로 미는 상황
    eat[sushi[i]] -= 1 # 초밥 빼기
    if eat[sushi[i]] == 0: # 처음 초밥 값이 0이 된다면,
        window -= 1 # 먹지 않은 종류가 되므로 -1
    
    other = sushi[(i + k) % N] # 초밥 추가, 회전하는 원형 벨트이므로 % N을 통해 원형 벨트를 구현
    if eat[other] == 0: # 다음 초밥이 한번도 먹지 않은 종류라면,
        window += 1 # 새로운 종류를 먹은 것이므로 +1
    eat[other] += 1
    
    if eat[c] == 0: # 쿠폰 초밥이 값이 0이라면 추가적으로 더 먹을 수 있으므로,
        cnt = max(cnt, window + 1)
    else:
        cnt = max(cnt, window)

print(cnt)

# set()함수 활용
import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

cnt = 0
for i in range(N):
    eat = set()
    for j in range(k):
        eat.add(sushi[(i + j) % N])
    if c not in eat:
        eat.add(c)
    cnt = max(cnt, len(eat))

print(cnt)