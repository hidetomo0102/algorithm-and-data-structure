"""
順列表示
Input: [1, 2, 3]
Output: (1, 2, 3)(1, 3, 2)(2, 1, 3)(2, 3, 1)(3, 1, 2)(3, 2, 1)
"""
from typing import List


def all_perms(elements: List[int]) -> List[List[int]]:
    if len(elements) < 2:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]
