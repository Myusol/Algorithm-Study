# 공유기 설치 / 골드4
import sys
input = sys.stdin.readline
N, C = map(int, input().split())
home = []
for _ in range(N):
    a = int(input())
    home.append(a)
home.sort()
# dist(임시 거리)로 이게 가능한지 확인
def greedy(dist):
    count = 1 # 첫 집에 설치하고 시작
    last_position = home[0]
    for i in range(1, N):
        if home[i] - last_position >= dist:
            count+=1
            last_position = home[i]
    return count >= C
left = 1 # 최소 거리
right = home[-1] - home[0] # 최대 거리
answer = 0
while left <= right:
    mid = (left + right) //2 # 중간값
    if greedy(mid):
        answer = mid # 가능한 경우를 저장하고 늘려서 다시
        left = mid + 1
    else: # 실패했으니 거리를 줄이고 다시
        right = mid - 1
print(answer)