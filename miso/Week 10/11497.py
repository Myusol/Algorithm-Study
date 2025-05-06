import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    L = sorted(list(map(int, input().split())))
    
    result = 0
    for i in range(0, N - 2):
        result = max(result, abs(L[i + 2] - L[i]))
        
    print(result)