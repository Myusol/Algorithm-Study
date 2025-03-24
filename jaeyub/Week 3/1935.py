N = int(input())
sentence = input()
num_list = []
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(N):
    num_list.append(int(input()))

stack = []

for c in sentence:
    if 'A' <= c <= 'Z':
        stack.append(num_list[alphabet.index(c)])
    else:
        b = stack.pop()
        a = stack.pop()
        
        if c=='+':
            stack.append(a+b)
        elif c=='-':
            stack.append(a-b)
        elif c=='*':
            stack.append(a*b)
        elif c=='/':
            stack.append(a/b)

print('%.2f' %stack[0])
