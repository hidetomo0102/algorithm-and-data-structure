# 108.Convert Sorted Array to Binary Search Tree
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, left: int, right: int, nums: list):
        if left > right:
            return None
        elif left == right:
            return TreeNode(nums[left])
        else:
            node = TreeNode(nums[(left + right) // 2])
            node.left = self.helper(left, ((left + right) // 2) - 1, nums)
            node.right = self.helper(((left + right) // 2) + 1, right, nums)

            return node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        if len(nums) == 2:
            node = TreeNode(nums[-1])
            node.left = TreeNode(nums[0])
            return node

        return self.helper(0, len(nums) - 1, nums)
