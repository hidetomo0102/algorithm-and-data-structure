from __future__ import annotations
from typing import Any, Optional


class Node:
    def __init__(self, data: Any, next_node: Node = None):
        self.data = data
        self.next = next_node


class LinkList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data: Any):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data: Any):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any):
        current_node = self.head

        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if not current_node:
            return

        previous_node.next = current_node.next
        current_node = None

    def reverse(self):
        previous_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def reverse_even(self):
        """
        連続する偶数のみリバースする
        """

        def _reverse_even(head: Node, previous_node: Optional[Node]):
            if not head:
                return

            current_node = head
            while current_node and current_node.data % 2 == 0:
                next_node = current_node.next
                current_node.next = previous_node

                previous_node = current_node
                current_node = next_node

            if current_node != head:
                head.next = current_node
                _reverse_even(current_node, None)
                return previous_node
            else:
                head.next = _reverse_even(head.next, head)
                return head

        self.head = _reverse_even(self.head, None)


link_list = LinkList()
link_list.insert(4)
link_list.append(3)
link_list.append(2)
link_list.print()  # 4 3 2
link_list.remove(3)
link_list.append(1)
link_list.print()  # 4 2 1
link_list.reverse()
link_list.print()  # 1 2 4
link_list.append(6)
link_list.reverse_even()
link_list.print()  # 1 6 4 2
