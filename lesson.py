# 169.Majority Element
from collections import Counter
from typing import List


def majorityElement(nums: List[int]) -> int:
    counter = Counter(nums)
    return counter.most_common()[0][0]
