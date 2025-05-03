import sys
input = sys.stdin.readline
N = int(input())
solution = sorted(list(map(int, input().split())))

val = int(1e10)
result = (0, 0)
l = 0
r = N - 1

while l < r:
    s = solution[l] + solution[r]
    if abs(s) < val:
        val = abs(s)
        result = (solution[l], solution[r])
    if s < 0:
        l += 1
    elif s > 0:
        r -=1
    else:
        break
    
print(*result)