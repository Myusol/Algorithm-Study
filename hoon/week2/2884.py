a,b=map(int,input().split())
if b < 45:
    a -= 1
    b = 45 - b
    b = 60 - b
elif b >= 45:
    b -= 45
if a == -1:
    a = 23

print(a, b)
