cases = int(input())

for case in range(cases):
    x1, y1, r1, x2, y2, r2 = [int(x) for x in input().split(' ')]

    # 만약 중심이 같다면
    if x1 == x2 and y1 == y2:
        if r1 == r2:  # 반지름도 같다면 무수히 많다
            print(-1)
        else:  # 반지름이 다르면 교점이 하나도 없다
            print(0)
    else:  # 중심이 다르다면
        # 거리에 따라 조건이 달라지지
        distance = ((x1 - x2)**2 + (y1 - y2)**2)**.5

        if r1 + r2 == distance or abs(r1 - r2) == distance:
            print(1)
        elif abs(r1 - r2) < distance < r1 + r2:
            print(2)
        else:
            print(0)

    continue
