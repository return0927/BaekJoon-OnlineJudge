# N - 카드개수
# M - 합의 목표
N, M = [int(x) for x in input().split(' ')]
cards = [int(x) for x in input().split(' ')]

# 파이썬에서는 카드의 수가 필요없는 대신 확신은 하자
assert len(cards) == N

finding = M / 3
ind = -1
for i in range(len(cards) - 1):
    assert finding >= cards[i]
    if cards[i] <= finding < cards[i+1]:
        found = True
        ind = i
        break

if ind < 0:  # 만약 기댓값이 카드들에 없다면 맨 끝 3개가 되겠지
    print(sum(cards[-3:]))
    exit()

assert ind <= len(cards) - 2  # 끝에 한 개의 원소가 더 있단걸 확인
for j in range(ind, -1, -1):
    if sum(cards[j-1:j+2]) <= M:
        print(sum(cards[j-1:j+2]))
        break
