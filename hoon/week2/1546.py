# M은 최댓값
n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
nscores = []
for i in range(n):
    nscores.append(scores[i]/m*100)
avg = sum(nscores)/len(scores)
print(avg)