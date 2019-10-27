x, y, w, h = [int(x) for x in input().split(' ')]
print(min(x, y, abs(w-x), abs(h-y)))
