a, b = [int(x) for x in input().split(" ")]
print("\n".join([ str(x) for x in [a+b, a-b, a*b, a//b, a%b]]))