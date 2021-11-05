"""
偶数を先に、奇数を後に並べる
[0, 1, 3, 4, 2, 4, 5, 1, 6, 2, 8] => [0, 4, 2, 4, 6, 8, 1, 3, 5, 1, 9]
"""
from typing import List


def order_even_first_odd_last(numbers: List[int]):
    i, j = 0, len(numbers) - 1
    while i < j:
        if numbers[i] % 2 == 0:
            i += 1
        else:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j -= 1
