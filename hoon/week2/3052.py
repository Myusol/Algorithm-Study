nums = []
for i in range(10):
    num = int(input())
    nums.append(num % 42)
uni = set(nums)
print(len(uni))