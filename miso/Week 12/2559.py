import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ondo = list(map(int, input().split()))

seq = 0
for i in range(K):
    seq += ondo[i]
    
result = seq
for i in range(N - K):
    seq += ondo[i + K] - ondo[i]
    result = max(result, seq)
    
print(result)