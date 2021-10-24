"""
Find most frequently appearing char
INPUT: 'I have a pen. I have an apple. Ah, Applepen!'
OUTPUT: ('a', 7)
"""
import operator
from collections import Counter

INPUT = 'I have a pen. I have an apple. Ah, Applepen!'


def find_frequent_char1(chars: str) -> tuple:
    """
    デフォルト辞書を使う
    """
    cache = {}
    for char in chars.lower():
        if char == " ":
            continue
        else:
            cache[char] = cache.get(char, 0) + 1
    max_key = max(cache, key=cache.get)
    return max_key, cache[max_key]


def find_frequent_char2(chars: str) -> tuple:
    """
    collections Counterを使う
    """
    c = Counter()
    for char in chars.lower():
        if not char.isspace():
            c[char] += 1
    max_key = max(c, key=c.get)
    return max_key, c[max_key]


def find_frequent_char3(chars: str) -> tuple:
    """
    operator itemgetterを使う
    """
    chars = chars.lower()
    l = []
    for char in chars:
        if not char.isspace():
            l.append((char, chars.count(char)))
    return max(l, key=operator.itemgetter(1))
