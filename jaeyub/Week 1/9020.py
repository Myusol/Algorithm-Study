num = 10000
a = [0,0] + [1] * (num-1)
primes = []


for i in range(2,num+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, num+1,i):
            a[j]= 0

N=int(input())

num_list=[int(input()) for _ in range(N)]


for num in num_list:
    if num == 4:
        print("2 2")
    else:
        if num % 4 == 0:
            A = num // 2 + 1
            B = num // 2 - 1
        else : 
            A = num // 2
            B = num // 2
        for _ in range(num//2):
            if A in primes and B in primes:
                print(B, A) 
                break
            else : 
                A = A + 2
                B = B - 2
