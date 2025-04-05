import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int,input().split()))
LIS = [0]

for x in num:
    if LIS[-1] < x:
        LIS.append(x)
    else:
        start=0
        end=len(LIS)

        while start<end:
            mid=(start+end)//2

            if LIS[mid] < x:
                start=mid+1
            else:
                end=mid
        LIS[end]=x
print(len(LIS)-1)