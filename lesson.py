import string
from typing import List


def snake_string_v1(chars: str) -> List[List[str]]:
    result = [[], [], []]
    result_idxes = {0, 1, 2}
    insert_idx = 0

    for i, s in enumerate(chars):
        if i % 4 == 1:
            insert_idx = 0
        elif i % 2 == 0:
            insert_idx = 1
        elif i % 4 == 3:
            insert_idx = 2

        result[insert_idx].append(s)
        for rest_idx in result_idxes - {insert_idx}:
            result[rest_idx].append(' ')
    return result


def snake_string_v2(chars: str, depth: int) -> List[List[str]]:
    """
    フレキシブルなスネーク表示関数

    :param chars: 並べたい文字列
    :param depth: 何段で表示するか
    """
    result = [[] for _ in range(depth)]
    result_idxes = {i for i in range(depth)}
    insert_idx = int(depth / 2)

    def positive(i):
        return i + 1

    def negative(i):
        return i - 1

    op = negative

    for c in chars:
        result[insert_idx].append(c)
        for rest_idx in result_idxes - {insert_idx}:
            result[rest_idx].append(' ')
        if insert_idx <= 0:
            op = positive
        if insert_idx >= depth - 1:
            op = negative
        insert_idx = op(insert_idx)

    return result


numbers = [str(i) for j in range(5) for i in range(10)]
chars = ''.join(numbers)
for line in snake_string_v1(chars):
    print(''.join(line))
    #  1   5   9   3   7   1   5   9   3   7   1   5   9
    # 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8
    #    3   7   1   5   9   3   7   1   5   9   3   7

alphabets = [s for _ in range(2) for s in string.ascii_lowercase]
strings = ''.join(alphabets)
for line in snake_string_v2(strings, 10):
    print(''.join(line))
    #      f                 x                 p
    #     e g               w y               o q
    #    d   h             v   z             n   r
    #   c     i           u     a           m     s
    #  b       j         t       b         l       t
    # a         k       s         c       k         u
    #            l     r           d     j           v
    #             m   q             e   i             w
    #              n p               f h               x z
    #               o                 g                 y
