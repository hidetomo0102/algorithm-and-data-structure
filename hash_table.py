import hashlib
from typing import Any, Optional, List, Tuple


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key: Any) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value):
        idx = self.hash(key)
        for data in self.table[idx]:
            # 既にあるkeyのvalueを変更
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[idx].append([key, value])

    def print(self):
        for idx in range(self.size):
            print(idx, end=' ')
            for data in self.table[idx]:
                print('-->', end=' ')
                print(data, end=' ')
            print()

    def get(self, key) -> Any:
        idx = self.hash(key)
        for data in self.table[idx]:
            if data[0] == key:
                return data[1]

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)


"""
1. Input: [11, 2, 5, 9, 10, 3], 12 => Output: (2, 10) or None
2. Input: [11, 2, 5, 9, 10, 3] (sum:20) => Output: (11, 9) or None
   ex) 11 + 9 = 2 + 5 + 10 + 3
"""


def get_pair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()
    for num in numbers:
        diff = target - num
        if diff in cache:
            return num, diff
        cache.add(num)


def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
    total = sum(numbers)
    half, residue = divmod(total, 2)
    # 合計 / 2が割りきれない場合は解なし
    if residue != 0:
        return

    cache = set()
    for num in numbers:
        diff = half - num
        if diff in cache:
            return num, diff
        cache.add(num)
