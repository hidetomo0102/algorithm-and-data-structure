# 160.Intersection of Two Linked Lists
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        nodes = set()
        p1 = headA
        while p1:
            nodes.add(p1)
            p1 = p1.next
        p1 = headB
        while p1:
            if p1 in nodes:
                return p1
            p1 = p1.next

        return None
