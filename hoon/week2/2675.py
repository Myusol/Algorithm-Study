a=int(input())
for _ in range(a):
    b,s= input().split()
    b = int(b)
    ss = []
    for char in s:
        ss.append(char*b)
    if ss:
        print(''.join(ss))