# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 모듈 날먹 버전
import math

a,b = map(int,input().split())

print(math.gcd(a,b))
print(math.lcm(a,b))


# 유클리드 호제법 버전
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

a,b = map(int,input().split())

print(gcd(a,b))
print(int(a*b/gcd(a,b)))