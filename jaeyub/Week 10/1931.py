import sys
input = sys.stdin.readline

N = int(input())
time = []
for i in range(N):
    start, end = map(int,input().split())
    time.append((start, end))

time.sort(key=lambda x : (x[1],x[0]))
count = 1
end = time[0][1]
for i in range(1, N):
    if time[i][0]>=end:
        end = time[i][1]
        count += 1

print(count)