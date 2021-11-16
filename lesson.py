from typing import List


def remove_duplicates(nums: List[int]) -> int:
    length = len(nums)
    duplicate_count = 0
    for i in reversed(range(1, length)):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
            duplicate_count += 1

    return length - duplicate_count


a = remove_duplicates([1, 1])
b = remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
