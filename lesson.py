"""
キャッシュデコレーターを作成
"""
from time import time


def cache_dec(f):
    cache = {}

    def _wrapper(n):
        if n not in cache:
            cache[n] = f(n)
            return f(n)
        else:
            return cache[n]

    return _wrapper


@cache_dec
def long_func(num: int) -> int:
    r = 0
    for i in range(100):
        r += num * i
    return r
