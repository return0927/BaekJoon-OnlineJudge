cases = int(input())

for run in range(cases):
    k = int(input())  # floor
    n = int(input())  # room

    matrix = [[*range(1, n+1)]] + [[1] + [0] * (n - 1)] * k

    for floor in range(1, k + 1):  # floor
        for room in range(1, n):  # room
            matrix[floor][room] = matrix[floor - 1][room] + matrix[floor][room - 1]

    print(matrix[k][n-1])
