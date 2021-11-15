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
from typing import List


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


print_pascal(pascal_triangle(5))
