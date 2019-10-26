cases = int(input())

for n in range(cases):
    H, W, N = [int(x) for x in input().split(' ')]

    height = (N - 1) % H + 1
    width = (N - 1) // H + 1

    print('{}{}{}'.format(height, '0' if width < 10 else '', width))
