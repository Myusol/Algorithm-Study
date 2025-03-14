a=int(input())
num = int(input())
lis=[]
while num > 0:
    lis.append(num%10)
    num//=10
print(sum(lis))