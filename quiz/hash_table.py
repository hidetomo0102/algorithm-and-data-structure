"""
Implements decorator to cache func
（キャッシュデコレーターで2回目の処理を高速化）
"""


def cache_dec(func):
    cache = {}

    def wrapper(n):
        # 引数 n をキーとして格納
        if n not in cache:
            cache[n] = func(n)

        return cache[n]

    return wrapper


@cache_dec
def long_func(num: int) -> int:
    r = 0
    for i in range(1000):
        r += num * i

    return r


"""
Input X: [1, 2, 3, 4, 4, 5, 5, 8, 10] Y: [4, 5, 5, 5, 6, 7, 8, 8, 10]
Output: X: [1, 2, 3, 4, 4, 10] Y: [5, 5, 5, 6, 7, 8, 8, 10]
"""
from typing import List
from collections import Counter


def min_count_remove(x: List[int], y: List[int]):
    x_counter = Counter(x)
    y_counter = Counter(y)

    for key, value in x_counter.items():
        y_count = y_counter.get(key)
        if y_count:
            if y_count > value:
                x[:] = [i for i in x if i != key]
            elif value > y_count:
                y[:] = [i for i in y if i != key]

    return x, y


a, b = min_count_remove([1, 2, 3, 4, 4, 5, 5, 8, 10], [4, 5, 5, 5, 6, 7, 8, 8, 10])
print(a, b)
