# 후위 표기식2 / 실버3
n = int(input())
post = input() # abc*+de/-
eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = {} # 1 2 3 4 5
stack = []
for i in range(n):
    nums[eng[i]] = int(input()) # a부터 순서대로 받음 value를 받음
for ch in post:
    if ch in nums: # 숫자 만나면 스택에 추가
        stack.append(nums[ch])
    else: # 연산자 만나면 연산시작
        a = stack.pop()
        b = stack.pop()
        if ch == '+':
            c = b + a
            stack.append(c)
        elif ch == '-':
            c = b - a
            stack.append(c)
        elif ch == '*':
            c = b * a
            stack.append(c)
        elif ch == '/':
            c = b / a
            stack.append(c)
# d = stack.pop()
# print(f'{d:.2f}')
print(f'{stack[0]:.2f}')