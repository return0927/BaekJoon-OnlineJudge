class Snail:
    def __init__(self):
        self.count = 0

    def resize(self, size):
        self.count = size
        return self.count

    def generate(self):
        for row in range(0, self.count):
            for column in range(0, self.count):
                depth = min(column, row, self.count - column - 1, self.count - row - 1)

                if column >= row:
                    _temp = column+row - 2*depth
                else:
                    _temp = (self.count-1 - 2*depth) * 4 - (column+row - 2*depth)
                _temp += 4 * (depth * self.count - depth ** 2)
                yield "{:3d}".format(_temp+1)
            yield "\n"


runner = Snail()
runner.resize(5)
print("".join(list(runner.generate())))