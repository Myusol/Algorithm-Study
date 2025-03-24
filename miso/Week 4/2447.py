import sys
def stars(n):
    if n==3:
        return['***','* *','***']
    l=[]
    star=stars(n//3)
    for i in star:
        l.append(i*3)
    for i in star:
        l.append(i+' '*(n//3)+i)
    for i in star:
        l.append(i*3)
    return l
n=int(sys.stdin.readline().strip())
print('\n'.join(stars(n)))