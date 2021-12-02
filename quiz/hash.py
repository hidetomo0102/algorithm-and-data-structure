"""
Symmetric
Input: [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
Output: [(5, 3), (7, 4)]
"""
from typing import List, Tuple


def find_symmetric(numbers: List[Tuple[int, int]]):
    cache = {}
    for num in numbers:
        first, second = num[0], num[1]
        value = cache.get(second)
        if not value:
            cache[first] = second
        elif value == first:
            yield num
