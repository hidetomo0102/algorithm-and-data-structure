"""
[1] => [2] => 2
[2, 3] => [2, 4] => 24
[9, 9] => [1, 0, 0] => 100
[7, 8, 9] => [7, 9, 0] => 790
"""
from typing import List


def remove_zero(numbers: List[int]):
    """
    先頭の数字に0を避ける
    """
    if numbers and numbers[0] == 0:
        numbers.pop(0)
        remove_zero(numbers)


def list_to_int(numbers: List[int]) -> int:
    sum_numbers = 0
    for i, num in enumerate(reversed(numbers)):
        sum_numbers += num * (10 ** i)

    return sum_numbers


def plus_one_list_to_int(numbers: List[int]) -> int:
    i = len(numbers) - 1
    numbers[i] += 1

    while i > 0:
        if numbers[i] != 10:
            remove_zero(numbers)
            break
        # 繰り上がりが発生するとき
        numbers[i] = 0
        numbers[i - 1] += 1
        i -= 1
    # 最後の桁の繰り上がりをチェック
    else:
        if numbers[0] == 10:
            numbers[0] = 1
            numbers.append(0)

    return list_to_int(numbers)


a = plus_one_list_to_int([9, 9, 9])
print(a)
