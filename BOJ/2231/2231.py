n = int(input())

creation = lambda n: n + sum([int(x) for x in list(str(n))])

for i in range(1, n+1):
    if n == creation(i):
        print(i)
        exit()
