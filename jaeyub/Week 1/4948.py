num = 123456 * 2
a = [0,0] + [1] * (num-1)


for i in range(2,num+1):
    if a[i]:
        # primes.append(i)
        for j in range(2*i, num+1,i):
            a[j]= 0

num_list=[]

while(True):
    x = int(input())
    if (x==0): break
    num_list.append(x)

for i in num_list:
    print(sum(a[i+1:i*2+1]))

