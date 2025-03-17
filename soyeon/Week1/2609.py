a, b = map(int, input().split())

def gcd_div(a, b):
    min_num = min(a, b)
    gcd = 1
    for i in range(1, min_num + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def lcm_div(a, b):
    gcd = gcd_div(a, b)
    return (a * b) // gcd

print(gcd_div(a, b))
print(lcm_div(a, b))