def check_prime(n: int) -> bool:
    if n == 1:
        return False
    for i in range(2, int(n**.5 + .5) + 1):
        if n % i == 0:
            return False
    return True


under, over = [int(x) for x in input().split(' ')]
primes = [*filter(lambda x: check_prime(x), [*range(under, over + 1)])]
print('\n'.join(str(x) for x in primes))
