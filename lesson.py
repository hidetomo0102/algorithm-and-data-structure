# 136.Single Number
from typing import List
from collections import Counter


def singleNumber(nums: List[int]) -> int:
    counter = Counter(nums)
    c = counter.most_common()
    return c[-1][0]
