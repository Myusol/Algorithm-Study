a=int(input())
for _ in range(a):
    lis = list(map(str,input()))
    print(''.join(map(str,lis[0],lis[-1])))