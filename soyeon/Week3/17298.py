import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
result = [-1] * n
stack = []

for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        idx = stack.pop()
        result[idx] = A[i]
    stack.append(i)

print(*result)