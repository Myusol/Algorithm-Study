import sys
input = sys.stdin.readline
N = int(input())

eratos = [1] * (N + 1)
eratos[0] = eratos[1] = 0
for i in range(2, int(N ** 0.5) + 1):
    if eratos[i]:
        for j in range(2 * i, N + 1, i):
            eratos[j] = 0
prime = [i for i, val in enumerate(eratos) if val]
            
start, end = 0, 0
cnt = 0
total = 0
while True:
    if total >= N:
        if total == N:
            cnt += 1
        total -= prime[start]
        start += 1
    elif end == len(prime):
        break
    else:
        total += prime[end]
        end += 1
        
print(cnt)