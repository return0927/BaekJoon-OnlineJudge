n = int(input())

creation = lambda n: n + sum(map(int, list(str(n))))

for i in range(1, n+1):
    if n == creation(i):
        print(i)
        exit()
print(0)
