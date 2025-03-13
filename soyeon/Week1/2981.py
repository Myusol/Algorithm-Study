import sys

n = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(n)]

nums.sort()

diff = [nums[i] - nums[i-1] for i in range(1, n)]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

gcd_value = diff[0]
for i in range(1, len(diff)):
    gcd_value = gcd(gcd_value, diff[i])

result = set()
for i in range(1, int(gcd_value**0.5) + 1):
    if gcd_value % i == 0:
        result.add(i)
        result.add(gcd_value // i)
        
result.discard(1)
print(*sorted(result))