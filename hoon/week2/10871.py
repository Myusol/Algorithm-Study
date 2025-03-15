a,b=map(int,input().split())
nums=list(map(int,input().split()))
numss=[]
for i in range(a):
    if b > nums[i]:
        numss.append(nums[i])
print(*numss)