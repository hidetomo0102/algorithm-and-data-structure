"""
順列表示
Input: [1, 2, 3]
Output: (1, 2, 3)(1, 3, 2)(2, 1, 3)(2, 3, 1)(3, 1, 2)(3, 2, 1)
"""
from typing import List


def all_perms(elements: List[int]) -> List[List[int]]:
    if len(elements) < 2:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


"""
1. Check palindrome
aba => True
abc => False
racecar => True

2. Find palindrome
abcracecarbda => cec, aceca, racecar
"""


def is_palindrome(char: str) -> bool:
    if not char:
        return False

    if len(char) == 1:
        return True

    start, end = 0, len(char) - 1
    while start < end:
        if char[start] != char[end]:
            return False
        start += 1
        end -= 1

    return True


def find_palindrome(char: str, left: int, right: int):
    while 0 <= left and right <= len(char) - 1:
        if char[left] != char[right]:
            break

        yield char[left: right + 1]
        left -= 1
        right += 1


def find_all_palindrome(strings: str):
    length = len(strings)

    if not length:
        yield

    if length == 1:
        yield strings

    for i in range(1, length - 1):
        yield from find_palindrome(strings, i - 1, i + 1)
        yield from find_palindrome(strings, i - 1, i)
