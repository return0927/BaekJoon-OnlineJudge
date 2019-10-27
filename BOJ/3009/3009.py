class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({})'.format(self)

    def __str__(self):
        return '{}, {}'.format(self.x, self.y)

    @property
    def len(self) -> float:
        return (self.x**2 + self.y**2)**.5

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)


A = Vector(*[int(x) for x in input().split(' ')])
B = Vector(*[int(x) for x in input().split(' ')])
C = Vector(*[int(x) for x in input().split(' ')])

AB = (A - B).len
BC = (B - C).len
AC = (A - C).len
diagonal = max(AB, BC, AC)

d_m, d_n, d_f = None, None, None

if diagonal == AB:
    last = A + B - C
elif diagonal == BC:
    last = B + C - A
else:  # CA
    last = A + C - B

print(last.x, last.y)
