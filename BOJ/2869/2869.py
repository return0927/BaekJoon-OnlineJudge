A, B, V = [int(x) for x in input().split(' ')]

abstract = (V - B) / (A - B)
print(int(abstract) + int(abstract != abstract//1))
