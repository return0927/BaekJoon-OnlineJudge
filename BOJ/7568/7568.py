def rank(entire: list):
    """동일한 값을 높은 등수로, 동알힌 값의 개수 반영 랭킹구하기"""
    ranks = [0, ] * len(entire)
    upper = sorted(entire)

    for i in range(len(entire)):
        ranks[i] = upper.index(entire[i]) + 1

    return ranks


N = int(input())

humans = []
for n in range(N):
    weight, height = map(int, input().split(' '))
    humans.append((weight, height))

# 전수조사 비교를 위한 2차원 배열 생성
matrix = [[False for x in range(N)] for y in range(N)]

# print(matrix)
# 전수조사 비교 시행
for i in range(N):
    mw, mh = humans[i]
    for j in range(N):
        w, h = humans[j]

        if mw > w and mh > h:
            matrix[j][i] = True

ranks = [x.count(True) + 1 for x in matrix]
print(" ".join(map(str, ranks)))
