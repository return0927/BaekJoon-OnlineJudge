cases = int(input())

for case in range(cases):
    x, y = [int(x) for x in input().split(' ')]
    distance = (y - x + 1 - 2) / 2 # 처음과 끝은 무조건 1로 가야한다
    count = 2
    prior = 1

    while distance:
        if distance <= prior:
            count += 1
            continue

