import sys
from typing import Optional


class MinHeap:
    def __init__(self):
        self.heap = [-1 * sys.maxsize]
        self.current_size = 0

    def push(self, value: int):
        self.heap.append(value)
        self.current_size += 1
        # 正しい順序に並べる
        self._heapify_up(self.current_size)

    def pop(self) -> Optional[int]:
        if len(self.heap) == 1:
            return

        root = self.heap[1]
        data = self.heap.pop()
        if len(self.heap) == 1:
            return root

        self.heap[1] = data
        self.current_size -= 1
        self._heapify_down(1)
        return root

    def _parent_index(self, idx: int) -> int:
        """
        親ノードのインデックス番号を返す
        """
        return idx // 2

    def _left_child_index(self, idx: int) -> int:
        """
        左にある子ノードのインデックス番号を返す
        """
        return 2 * idx

    def _right_child_index(self, idx: int) -> int:
        """
        右にある子ノードのインデックス番号を返す
        """
        return (2 * idx) + 1

    def _min_child(self, idx: int) -> int:
        """
        子ノードのうち最小のもののインデックス番号を返す
        """
        if self._right_child_index(idx) > self.current_size:
            return self._left_child_index(idx)
        else:
            if self.heap[self._left_child_index(idx)] < self.heap[self._right_child_index(idx)]:
                return self._left_child_index(idx)
            else:
                return self._right_child_index(idx)

    def _swap(self, idx1: int, idx2: int):
        """
        ノード同士を入れ替える
        """
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def _heapify_up(self, idx: int):
        """
        最小ノードが親になるまで押し上げる
        """
        while self._parent_index(idx) > 0:
            if self.heap[idx] < self.heap[self._parent_index(idx)]:
                self._swap(idx, self._parent_index(idx))
            idx = self._parent_index(idx)

    def _heapify_down(self, idx: int):
        """
        最大ノードが子になるまで押し下げる
        """
        while self._left_child_index(idx) <= self.current_size:
            min_child_idx = self._min_child(idx)
            if self.heap[idx] > self.heap[min_child_idx]:
                self._swap(idx, min_child_idx)
            idx = min_child_idx
