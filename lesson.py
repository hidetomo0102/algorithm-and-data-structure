# 118.Pascal's Triangle
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        data = [[1] * (i + 1) for i in range(numRows)]

        for line in range(2, numRows):
            for i in range(1, line):
                data[line][i] = data[line - 1][i - 1] + data[line - 1][i]

        return data


s = Solution()
s.generate(5)
