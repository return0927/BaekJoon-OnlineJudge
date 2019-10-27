def check_prime(n: int) -> bool:
    if n == 1:
        return False
    for i in range(2, int(n**.5 + .5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
# eratos = [False, False, True]
while n:
    # TLE 15856468
    # primes = [*filter(lambda x: check_prime(x), [*range(n, 2*n+1)])]

    # TLE 15856468
    count = 0
    for i in range(n + 1, 2*n+1):
        count += check_prime(i)
    print(count)
    n = int(input())
