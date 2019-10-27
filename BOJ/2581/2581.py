def check_prime(n: int) -> bool:
    if n == 1:
        return False
    for i in range(2, int(n**.5 + .5) + 1):
        if n % i == 0:
            return False
    return True


# 1 <= under, over <= 10000
under, over = int(input()), int(input())

primes = [*filter(lambda x: check_prime(x), [*range(under, over + 1)])]

if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)
