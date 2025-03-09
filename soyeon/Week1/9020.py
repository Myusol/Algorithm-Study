def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    return is_prime

def find_goldbach_partition(n, is_prime):
    for i in range(n // 2, 1, -1):
        if is_prime[i] and is_prime[n - i]:
            return i, n - i

t = int(input().strip())
numbers = [int(input().strip()) for _ in range(t)]

limit = max(numbers)
is_prime = sieve_of_eratosthenes(limit)

for n in numbers:
    p1, p2 = find_goldbach_partition(n, is_prime)
    print(p1, p2)
