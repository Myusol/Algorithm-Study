import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

visited = [0] * 100001
start = 0
end = 0
result = 0

while start < n:
    while end < n and visited[a[end]] == 0:
        visited[a[end]] = 1
        end += 1
    result += end - start
    visited[a[start]] = 0
    start += 1

print(result)