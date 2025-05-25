import sys
input =sys.stdin.readline

N = int(input())
pList = []
arr = [False, False] + [True] * (N-1)

for i in range(2, N+1) :
    if arr[i] :
        pList.append(i)
    for j in range(i*i, N+1, i) :
        arr[j] = False

sum = 0
cnt = 0
start = 0
end = 0

while True :
    if sum >= N :
        if sum == N :
            cnt += 1
        sum -= pList[start]
        start += 1
    elif end == len(pList) :
        break
    else :
        sum += pList[end]
        end += 1
print(cnt)