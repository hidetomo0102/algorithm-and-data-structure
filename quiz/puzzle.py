"""
ハノイの塔
"""


def hanoi(disk: int, src: str, dest: str, support: str):
    if disk < 1:
        return

    hanoi(disk - 1, src, support, dest)
    print(f'move {disk} from {src} to {dest}')
    hanoi(disk - 1, support, dest, src)


"""
パスカルの三角形
"""
from typing import List, Optional


def pascal_triangle(depth: int) -> List[List[int]]:
    data = [[1] * (i + 1) for i in range(depth)]
    for line in range(2, depth):
        for i in range(1, line):
            data[line][i] = data[line - 1][i - 1] + data[line - 1][i]

    return data


def print_pascal(data: List[List[int]]):
    max_digit = max(data[-1])
    # 偶数にしないとズレるので調整
    width = max_digit + (max_digit % 2) + 2

    for index, line in enumerate(data):
        numbers = ''.join([str(i).center(width, ' ') for i in line])
        print((' ' * int(width / 2)) * (len(data) - index), numbers)


"""
トライアングルの最小合計パス
Input 5, 20
Output [[7], [6, 3], [6, 0, 15], [4, 20, 1, 8], [6, 4, 4, 1, 0]], 11
"""
import random


def generate_triangle_list(depth: int, max_num: int) -> List[List[int]]:
    return [[random.randint(0, max_num) for _ in range(i)] for i in range(1, depth + 1)]


def print_triangle(data: List[List[int]]):
    max_digit: int = len(str(max([max(l) for l in data])))
    width: int = max_digit + (max_digit % 2) + 2
    for index, line in enumerate(data):
        numbers = ''.join([str(i).center(width, ' ') for i in line])
        print(' ' * int(width / 2) * (len(data) - index), numbers)


def sum_min_path(triangle: List[List[int]]) -> Optional[int]:
    tree_sum = triangle[:]
    j, len_triangle = 1, len(triangle)
    if not len_triangle:
        return

    while j < len_triangle:
        line = triangle[j]
        line_path_sum = []
        for i, value in enumerate(line):
            if i == 0:
                sum_value = line[i] + tree_sum[j - 1][0]
            elif i == len(line) - 1:
                sum_value = line[i] + tree_sum[j - 1][i - 1]
            else:
                min_path = min(tree_sum[j - 1][i - 1], tree_sum[j - 1][i])
                sum_value = line[i] + min_path
            line_path_sum.append(sum_value)

        tree_sum[j] = line_path_sum
        j += 1
    return min(tree_sum[-1])


data = generate_triangle_list(5, 20)
print_triangle(data)
print(sum_min_path(data))
