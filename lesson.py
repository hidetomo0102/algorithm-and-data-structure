# 167.Two Sum II - Input Array Is Sorted
from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    N = len(numbers)
    lookup = {}

    for i in range(N):
        residue = target - numbers[i]

        if residue not in lookup:
            lookup[numbers[i]] = i
        else:
            return [lookup[residue] + 1, i + 1]
