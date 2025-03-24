import sys
def cantor(n):
    if n==0:
        return ['-']
    l=[]
    cant=cantor(n-1)
    for i in cant:
        l.append(i+' '*(3**(n-1))+i)
    return l
while True:
    try:
        n=int(sys.stdin.readline())
        print(''.join(cantor(n)))
    except:
        break
