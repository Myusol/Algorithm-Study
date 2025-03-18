import sys
oper=['+','-','*','/']
notation=[]
n=int(input())
postfix=sys.stdin.readline().strip()
val=[int(input()) for _ in range(n)]
for i in range(len(postfix)):
    if postfix[i] not in oper:
        n=ord(postfix[i])-ord('A')
        notation.append(val[n])
    else:
        y=notation.pop()
        x=notation.pop()
        notation.append(eval(f'{x}{postfix[i]}{y}'))
print(f'{notation[-1]:.2f}')