# 2.Add Two Numbers
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        tail = None

        while l1 or l2:
            if l1 and l2:
                sums = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sums = l1.val + carry
                l1 = l1.next
            else:
                sums = l2.val + carry
                l2 = l2.next

            carry = 0
            if sums > 9:
                carry = sums // 10

            num = sums % 10
            if not head:
                head = ListNode(num)
                tail = head
            else:
                tail.next = ListNode(num)
                tail = tail.next

        while carry != 0:
            tail.next = ListNode(carry % 10)
            tail = tail.next
            carry //= 10

        return head
