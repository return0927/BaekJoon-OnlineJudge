cases = int(input())


###########################################################
# Code from https://gist.github.com/endolith/114336/eff2dc13535f139d0d6a2db68597fad2826b53c3
def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)
###########################################################


def custom_iter(m, n):
    limit = lcm(m, n)
    m = [*range(1, m+1)]
    n = [*range(1, n+1)]

    count = 0
    while count <= limit:
        count += 1
        a, m = m[0], m[1:] + [m[0]]
        b, n = n[0], n[1:] + [n[0]]

        yield a, b

    yield -1, -1


for run in range(cases):
    M, N, x, y = [int(x) for x in input().split(' ')]

    _lcm = lcm(M, N)

    count = 0
    found = False
    for a, b in custom_iter(M, N):
        if a == -1 or b == -1:
            break

        count += 1
        if a == x and b == y:
            print(count)
            found = True
            break

    if found:
        continue
    print(-1)
