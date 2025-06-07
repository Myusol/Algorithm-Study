import sys
input = sys.stdin.readline
N = int(input())
alphabet = [list(input().strip()) for _ in range(N)]
    
weight = {}

for a in alphabet:
    l = len(a) - 1
    for i in range(l + 1):
        if a[i] in weight:
            weight[a[i]] += 10 ** (l - i)
        else:
            weight[a[i]] = 10 ** (l - i)

weight = sorted(weight.values(), reverse=True)
num = 9
t = 0

for i in weight:
    t += i * num
    num -= 1
    
print(t)