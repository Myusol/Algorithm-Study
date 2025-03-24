n = int(input())
paper = [[0] * 100 for _ in range(100)]

for _ in range(n):
    a, b = map(int,input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            paper[i][j] = 1
            
size = 0
for i in range(100):
    size += sum(paper[i])

print(size)