"""
[1] => [2] => 2
[2, 3] => [2, 4] => 24
[8, 9] => [9, 0] => 90
[0, 9, 9] => [1, 0, 0] => 100
"""

from typing import List


def remove_zero(numbers: List[int]):
    """
    足し算したリストの先頭に0が入らないようにする
    """
    if numbers and numbers[0] == 0:
        numbers.pop(0)
        remove_zero(numbers)


def list_to_int(numbers: List[int]) -> int:
    x = 10 ** (len(numbers) - 1)
    ans = 0
    for num in numbers:
        ans += num * x
        x /= 10
    return int(ans)


def list_plus1_to_int(numbers: List[int]) -> int:
    last_idx = len(numbers) - 1
    numbers[last_idx] += 1
    while 0 < last_idx:
        if numbers[last_idx] != 10:
            remove_zero(numbers)
            break
        # 繰り上がりが発生するとき
        numbers[last_idx] = 0
        numbers[last_idx - 1] += 1
        last_idx -= 1
    else:
        if numbers[0] == 10:
            numbers[0] = 1
            numbers.append(0)
    print(numbers)

    return list_to_int(numbers)


a = list_plus1_to_int([9, 9])
b = list_plus1_to_int([7, 8, 9])
print(a)  # 100
print(b)  # 790
