from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for i in range(m, m + n):
        j = i - m
        nums1[i] = nums2[j]
    nums1[:] = sorted(nums1)


merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
