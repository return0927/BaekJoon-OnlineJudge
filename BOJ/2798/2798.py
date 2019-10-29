from itertools import combinations

# N - 카드개수
# M - 합의 목표
N, M = [int(x) for x in input().split(' ')]
cards = [int(x) for x in input().split(' ')]
cards.sort()

# 파이썬에서는 카드의 수가 필요없는 대신 확신은 하자
assert len(cards) == N

last = 0
for s in combinations(cards, 3):
    su = sum(s)
    if M >= su > last:
        last = su

print(last)
