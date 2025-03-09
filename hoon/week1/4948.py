def sieve_eratosthenes(n):
    sieve = [True] * (n+1)
    sieve[0], sieve[1] = False, False

    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return sieve

max_val = 123456 * 2
prime_sieve = sieve_eratosthenes(max_val)

while True:
    n = int(input()) # 10
    if n == 0:
        break
    m = n * 2
    count = 0

    for i in range(n+1, m+1):
        if prime_sieve[i]:
            count += 1
    print(count)