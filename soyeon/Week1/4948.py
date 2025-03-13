def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    return is_prime

def count_primes_in_range(n, primes):
    return sum(primes[n+1:2*n+1])

MAX_N = 123456
primes = sieve_of_eratosthenes(2 * MAX_N)  # 2n까지 소수 구하기

while True:
    n = int(input())
    if n == 0:
        break
    print(count_primes_in_range(n, primes))