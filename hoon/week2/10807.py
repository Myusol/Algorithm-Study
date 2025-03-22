a=int(input())
nums=list(map(int,input().split()))
v=int(input())
count=0
for i in range(a):
    if v == nums[i]:
        count+=1
print(count)