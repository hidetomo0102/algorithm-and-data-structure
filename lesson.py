# 191.Number of 1 Bits
from collections import Counter


def hammingWeight(n: int) -> int:
    n = bin(n)
    counter = Counter(n)
    return counter.get("1", 0)
