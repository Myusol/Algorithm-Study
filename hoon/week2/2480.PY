a,b,c=map(int,input().split())
if a == b == c:
    a = 10000 + (a * 1000)
    print(a)
elif a == b or a == c:
    a = 1000 + (a * 100)
    print(a)
elif b == c:
    b = 1000 + (b * 100)
    print(b)
else:
    print(max(a,b,c) * 100)
