a, b = map(int, input().split())
# 최대공약수 구하기
# 각 수의 약수를 구해서 공통된 가장 높은 수를 구할것
def gcd_math(a, b):
    max_common = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            max_common = i
    return max_common

gcd = gcd_math(a, b)
# 최소공배수 구하기
# 각 수의 배수를 구해서 공통된 가장 작은 수를 구할것
def lcm_math(a, b):
    maxi = max(a, b)
    while True:
        if maxi % a == 0 and maxi % b == 0:
            return maxi
        else:
            maxi += max(a, b)

lcm = lcm_math(a, b)

print(gcd)
print(lcm)
