a, b, c = sorted([int(x) for x in input().split(' ')])
while a + b + c:
    print('right' if a**2 + b**2 == c**2 else 'wrong')
    a, b, c = sorted([int(x) for x in input().split(' ')])
