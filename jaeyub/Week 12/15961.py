import sys
input = sys.stdin.readline

N,D,K,C = map(int,input().split())

visited = [0] * (D+1)
visited[C] = 1
count = 1

chobab = []
for _ in range(N):
    chobab.append(int(input()))

for i in range(K):
    if visited[chobab[i]] == 0:
        count+=1
    visited[chobab[i]] += 1

answer = count
for start in range(N):
    end = (start + K) % N
    
    if visited[chobab[end]] == 0:
        count+=1
    visited[chobab[end]]+=1

    if visited[chobab[start]] == 1:
        count-=1
    visited[chobab[start]]-=1

    answer = max(answer, count)
    
print(answer)