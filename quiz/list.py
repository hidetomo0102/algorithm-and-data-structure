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


"""
スネーク表示
"""


def list_to_snake(result: List[List[str]]):
    for line in result:
        print(''.join(line))


def snake_string_v1(chars: str):
    result = [[], [], []]
    result_indexes = {0, 1, 2}

    insert_index = 1

    for i, char in enumerate(chars):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2

        result[insert_index].append(char)
        for rest in result_indexes - {insert_index}:
            result[rest].append(' ')

    list_to_snake(result)


def snake_strings_v2(chars: str, depth: int):
    result = [[] for _ in range(depth)]
    result_indexes = {i for i in range(depth)}
    insert_index = int(depth / 2)

    def pos(i):
        return i + 1

    def neg(i):
        return i - 1

    ops = neg

    for c in chars:
        result[insert_index].append(c)
        for rest in result_indexes - {insert_index}:
            result[rest].append(" ")

        if insert_index <= 0:
            ops = pos

        if insert_index >= depth - 1:
            ops = neg

        insert_index = ops(insert_index)

    return result


"""
1. Maximum subarray sum
Input: [1, -2, 3, 6, -1, 2, 4, -5, 2]
Output: 14

2. Maximum circular subarray sum
Input: [1, -2, 3, 6, -1, 2, 4, -5, 2]
Output: 15
"""


def get_sequence_sum(numbers: List[int], ops) -> int:
    result, sum_sequence = 0, 0
    for num in numbers:
        # 累積和 + num > numなら継続
        sum_sequence = ops(num, num + sum_sequence)
        result = ops(result, sum_sequence)

    return result


def get_max_circular_sum(numbers: List[int]) -> int:
    # 全体の合計値からmin_sequence_sumを引いてあげる
    total = sum(numbers)
    return total - get_sequence_sum(numbers, min)
