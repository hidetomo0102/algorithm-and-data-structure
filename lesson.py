# 110.Balanced Binary Tree
from typing import Optional
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        s = deque()
        s.appendleft((root, -1, 0))

        r = deque()

        while s:
            node, parent, LR = s.popleft()
            r.appendleft((node, parent, LR))

            if node.right:
                s.appendleft((node.right, node, 1))
            if node.left:
                s.appendleft((node.left, node, 0))

        heights = defaultdict(lambda: [0, 0])
        while r:
            node, parent, LR = r.popleft()
            node_heights = heights.get(node, [0, 0])
            if abs(node_heights[0] - node_heights[1]) > 1:
                return False
            heights[parent][LR] = max(node_heights) + 1

        return True
