# from datetime import datetime


def check_prime(n: int) -> bool:
    if n == 1:
        return False
    for i in range(2, int(n**.5 + .5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
eratos = [False, False, True]
while n:
    # s = datetime.now()
    # Extend book
    # print(len(eratos), n)
    if len(eratos) - 1 < 2*n:
        eratos += [True] * (2*n + 1 - len(eratos))

    for i in range(2*n):
        if eratos[i]:
            for j in range(2, int(2*n/i) + 1):
                # print(i, j, i * j, n, len(eratos))
                eratos[i * j] = False

    # print("E", eratos)
    # print("E", "{}~{}".format(n+1, 2*n), eratos[n+1:2*n+1])
    print(len([*filter(lambda x: x, eratos[n+1:2*n+1])]))
    # print(datetime.now() - s)

    n = int(input())
