"""
ある値が2つのリストに出現したとき、出現回数が少ない方のリストから削除する
（もし両方のリストに同数ある場合はスキップ）

INPUT X: [1, 2, 3, 4, 4, 5, 5, 8, 10] Y: [4, 5, 5, 5, 6, 7, 8, 8, 10]
  =>  X: [1, 2, 3, 4, 4, 10] Y: [5, 5, 5, 6, 7, 8, 8, 10]
"""
from typing import List
from collections import Counter

ans_x = []
ans_y = []


def min_count_remove(x: List[int], y: List[int]):
    x_counter = Counter(x)
    y_counter = Counter(y)

    for x_key, x_value in x_counter.items():
        y_value = y_counter.get(x_key)
        if y_value:
            if x_value < y_value:
                # そのkey以外の要素でリストを置き換える
                x[:] = [i for i in x if i != x_key]
            elif x_value > y_value:
                y[:] = [i for i in y if i != x_key]
    return x, y


x, y = min_count_remove([1, 2, 3, 4, 4, 5, 5, 8, 10], [4, 5, 5, 5, 6, 7, 8, 8, 10])
print(x, y)
