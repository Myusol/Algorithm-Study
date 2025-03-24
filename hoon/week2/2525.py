a,b=map(int,input().split())
c=int(input())

d = b + c

if d > 60:
    a = a + (d // 60)
    b = d % 60
elif d < 60:
    b = d
elif d == 60:
    a += 1
    b = 0
if a > 23:
    a -= 24
print(a,b)
