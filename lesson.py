"""
1. Check palindrome
aba => True
abc => False
racecar => True

2. Find palindrome
abcracecarda => cec, aceca, rcecar
"""
from typing import Generator


def check_palindrome_v1(chars: str) -> bool:
    if chars == chars[::-1]:
        return True
    return False


def check_palindrome_v2(chars: str) -> bool:
    len_char = len(chars)
    if not len_char:
        return False
    if len_char == 1:
        return True

    start, end = 0, len_char - 1
    while start < end:
        if chars[start] != chars[end]:
            return False
        start += 1
        end -= 1

    return True


def find_palindrome(chars: str) -> Generator:
    len_chars = len(chars)

    if not len_chars:
        yield

    if len_chars == 1:
        yield chars

    def _find_palindrome(chars: str, left: int, right: int) -> Generator:
        while 0 <= left and right <= len(chars) - 1:
            if chars[left] != chars[right]:
                break

            yield chars[left:right + 1]
            left -= 1
            right += 1

    for i in range(1, len_chars - 1):
        yield from _find_palindrome(chars, i - 1, i + 1)  # 奇数の場合
        yield from _find_palindrome(chars, i - 1, i)  # 偶数の場合


for s in find_palindrome("cabac"):
    print(s)
