# push x: x넣기
# pop: 가장 위 삭제하면서 출력, 없으면 -1출력
# size: 스택에 들어있는 정수 출력
# empty: 비어있으면 1 아니면 0
# top: 가장 위 정수 출력, 없으면 -1 출력
import sys
stack = []
input = sys.stdin.readline
a = int(input())
result = []
for _ in range(a):
    b = input().split()
    if len(b) == 2:
        s, num = b[0], b[1]
    else:
        s = b[0]
    
    if s == 'push':
        stack.append(num)
    elif s == 'pop':
        if len(stack) > 0:
            result.append(stack[-1])
            stack.pop()
        else:
            result.append(-1)
    elif s == 'size': 
        result.append(len(stack))
    elif s == 'empty':
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    elif s == 'top':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[-1])