from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    if target <= nums[0]:
        return 0

    if target > nums[len(nums) - 1]:
        return len(nums)

    def _search(left: int, right: int, target: int):
        if left >= right:
            if nums[left] < target:
                return left + 1
            else:
                return left

        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return _search(mid + 1, right, target)
        else:
            return _search(left, mid - 1, target)

    return _search(1, len(nums) - 1, target)


c = searchInsert([1, 2, 4, 6, 7], 3)
print(c)
