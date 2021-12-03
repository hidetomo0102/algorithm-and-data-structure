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
