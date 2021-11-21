from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    prev = None

    while current:
        if prev and current.val == prev.val:
            prev.next = current.next
        else:
            prev = current
        current = current.next

    return head
