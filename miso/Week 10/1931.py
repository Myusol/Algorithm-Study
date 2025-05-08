import sys
input = sys.stdin.readline
N = int(input())
hour = []

for _ in range(N):
    hour.append(list(map(int, input().split())))
    
hour.sort(key=lambda x:(x[1], x[0]))
meeting = hour[0][1]
cnt = 1

for i in range(1, N):
    if meeting <= hour[i][0]:
        cnt += 1
        meeting = hour[i][1]
        
print(cnt)