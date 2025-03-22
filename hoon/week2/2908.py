# 상수 / 브론즈2
# 입력 받은 수를 거꾸로 봐서 처음 나온걸로
a,b = map(str,input().split())
c = int(''.join(reversed(a)))
d = int(''.join(reversed(b)))
if c > d:
    print(c)
else:
    print(d)