# 최대공약수 함수 (유클리드 호제법)
def gcd(x,y):
	if(y == 0):
		return x
	else:
		return gcd(y, x%y)

x,y = map(int,input().split())

gcd = gcd(x,y)
lcm = x*y // gcd

print(gcd)
print(lcm)



