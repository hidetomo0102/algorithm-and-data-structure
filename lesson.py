"""
リスト内の要素を重複させない
[1, 3, 3, 5, 7, 7, 7, 10, 12, 12 ,15] => [1, 3, 5, 7, 10, 12, 15]
"""
from typing import List


def delete_duplicate_v1(numbers: List[int]):
    tmp = []
    for num in numbers:
        if num not in tmp:
            tmp.append(num)
    numbers[:] = tmp


def delete_duplicate_v2(numbers: List[int]):
    tmp = [numbers[0]]
    i, len_num = 0, len(numbers) - 1
    while i < len_num:
        if numbers[i] != numbers[i + 1]:
            tmp.append(numbers[i + 1])
        i += 1
    numbers[:] = tmp


def delete_duplicate_v3(numbers: List[int]):
    i = len(numbers) - 1
    while i > 0:
        if numbers[i] == numbers[i - 1]:
            numbers.pop(i)
        i -= 1


numbers = [1, 3, 3, 5, 7, 7, 7, 10, 12, 12, 15]
delete_duplicate_v3(numbers)
print(numbers)  # [1, 3, 5, 7, 10, 12, 15]
