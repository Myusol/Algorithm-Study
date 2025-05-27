N = int(input())

a = [0,0] + [1] * (N-1)
primes = []
for i in range(2,N+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, N+1,i):
            a[j]= 0

left, right = 0,1
answer=0

while right<=len(primes) and left<=right:
    total = sum(primes[left:right])

    if total == N:
        answer += 1
        right += 1

    elif total < N:
        right += 1
    else:
        left += 1

print(answer)