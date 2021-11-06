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


"""
Input: ['h', 'y', 'n', 'p', 't', 'o'], [3, 1, 5, 0, 2, 4]
Output: python
"""
from typing import List


def order_change_by_indexes_v1(chars: List[str], indexes: List[int]) -> str:
    tmp = [None] * len(chars)
    for i, index in enumerate(indexes):
        tmp[index] = chars[i]
    return "".join(tmp)


def order_change_by_indexes_v2(chars: List[str], indexes: List[int]) -> str:
    i, len_indexes = 0, len(indexes) - 1
    while i < len_indexes:
        while i != indexes[i]:
            idx = indexes[i]
            # 文字とインデックスを入れ替え
            chars[idx], chars[i] = chars[i], chars[idx]
            indexes[idx], indexes[i] = indexes[i], indexes[idx]
        i += 1

    return "".join(chars)


print(order_change_by_indexes_v2(['h', 'y', 'n', 'p', 't', 'o'], [3, 1, 5, 0, 2, 4]))
