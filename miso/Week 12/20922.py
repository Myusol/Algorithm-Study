import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))

seq = defaultdict(int)
start, end, maxlen = 0, 0, 0

while end < N:
    seq[a[end]] += 1
    
    while seq[a[end]] > K:
        seq[a[start]] -= 1
        start += 1
        
    maxlen = max(maxlen, end - start + 1)
    end += 1

print(maxlen)