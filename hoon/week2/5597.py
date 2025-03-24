nums = set() # 중복제거
for _ in range(28):
    num = int(input())
    nums.add(num)
mis = []
for i in range(1,31):
    if i not in nums:
        mis.append(i)
print(mis[0])
print(mis[1])