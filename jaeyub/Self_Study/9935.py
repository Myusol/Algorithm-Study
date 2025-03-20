import sys

S = sys.stdin.readline().rstrip()
explode = sys.stdin.readline().rstrip()

stack = []
e = len(explode)

for c in S:
    stack.append(c)
    if ''.join(stack[-e:]) == explode:
        for _ in range(e):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')