# 119.Pascal's Triangle II
from typing import List


def getRow(rowIndex: int) -> List[int]:
    data = [[1] * (i + 1) for i in range(rowIndex + 1)]

    for line in range(2, rowIndex + 1):
        for i in range(1, line):
            data[line][i] = data[line - 1][i - 1] + data[line - 1][i]

    return data[rowIndex]


a = getRow(1)
print(a)
