N = int(input())
numbers = list(map(int, input().split()))

start, end = 0,0
answer = 0
visited = [False]*100001

while start <= end and end < N:
    if not visited[numbers[end]]:
        visited[numbers[end]] = True
        answer += end-start+1
        end += 1
    else:
        while visited[numbers[end]]:
            visited[numbers[start]] = False
            start+=1

print(answer)