import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    s = list(map(int, input().split()))
    money, p = 0, 0
    
    for i in range(N - 1, -1, -1):
        if s[i] > p:
            p = s[i]
            
        else:
            money += p - s[i]
            
    print(money)