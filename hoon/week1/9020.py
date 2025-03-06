# T받아서 소수끼리 더해서 값을 만드는것을 출력하라
# 두소수의 값 차이가 작은것을 출력

#에라토스테네스의 체 연습
def sieve_eratosthenes(n):
    sieve = [True] * (n+1) # N 만큼 True로 모두 리스트로 저장
    sieve[0], sieve[1] = False, False # 0, 1 은 제외

    for i in range(2, int(n**0.5)+1): # 2부터 N루트 까지만 반복
        if sieve[i]: 
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i in range(n+1) if sieve[i]]


T = int(input())
max_n = 10000
primes = sieve_eratosthenes(max_n)
prime_set = set(primes)

for _ in range(T):
    n = int(input())
    a = n // 2
    b = n // 2
    while a > 1:
        if a in prime_set and b in prime_set:
            print(a, b)
            break
        a -= 1
        b += 1
