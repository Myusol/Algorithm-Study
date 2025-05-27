N, K = map(int, input().split())
temp = list(map(int, input().split()))

total = sum(temp[:K])
answer = total

for i in range(N-K):
    total += temp[K+i] - temp[i]
    answer = max(answer, total)

print(answer)