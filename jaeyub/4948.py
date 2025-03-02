def is_prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

num_list = []

while(True):
    n = int(input())
    if n==0:
        break
    num_list.append(n)

for i in num_list:
    prime = 0
    for j in range(i+1,2*i+1):
        if is_prime(j):
            prime +=1
    print(prime)