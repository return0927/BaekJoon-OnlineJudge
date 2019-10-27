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


for run in range(cases):
    M, N, x, y = [int(x) for x in input().split(' ')]
    limit = lcm(M, N)

    if x == y:
        print(x)
        continue

    if M > N:
        t = x
        count = x
        found = False

        while count <= limit and not found:
            count += M
            t = (t + M - 1) % N + 1
            # print(count, t)
            if t == y:
                found = True
                print(count)

        if not found:
            print(-1)

    else:
        t = y
        count = y
        found = False

        while count <= limit and not found:
            count += N
            t = (t + N - 1) % M + 1
            # print(count, t)
            if t == x:
                found = True
                print(count)

        if not found:
            print(-1)
