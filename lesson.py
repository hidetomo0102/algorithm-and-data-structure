# 141.Linked List Cycle
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False

    p = head
    while p:
        if p.val == "v":
            return True
        p.val = "v"
        p = p.next

    return False
