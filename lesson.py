from typing import List


def removeElement(nums: List[int], val: int) -> int:
    nums[:] = [i for i in nums if i != val]
    return len(nums)


a = removeElement([3, 2, 2, 3], 3)
b = removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
