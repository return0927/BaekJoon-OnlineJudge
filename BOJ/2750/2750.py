from typing import List


# Bubble Sort O(n^2)
def bubble(data: List[int]) -> List[int]:
    n = len(data)
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data


nums = [*map(int, [input() for i in '*'*int(input())])]
nums = bubble(nums)
print('\n'.join(map(str, nums)))
