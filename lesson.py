from typing import List


def maxSubArray(nums: List[int]) -> int:
    result_sequence, sum_sequence = nums[0], 0
    for num in nums:
        sum_sequence = max(num, sum_sequence + num)
        result_sequence = max(result_sequence, sum_sequence)

    return result_sequence


a = maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
b = maxSubArray([5, 4, -1, 7, 8])
c = maxSubArray([-1])
print(a)
print(b)
print(c)
