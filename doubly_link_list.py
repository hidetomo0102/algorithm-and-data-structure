from __future__ import annotations
from typing import Any


class Node:
    def __init__(self, data: Any, next_node: Node = None, prev_node: Node = None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class LinkList:
    def __init__(self, head: Node = None):
        self.head = head

    def append(self, data: Any):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node

    def insert(self, data: Any):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any):
        current_node = self.head
        # 先頭に一致
        if current_node and current_node.data == data:
            if current_node.next is None:
                self.head = None
                current_node = None
                return
            else:
                next_node = current_node.next
                next_node.prev = None
                self.head = next_node
                current_node = None
                return

        while current_node and current_node.data != data:
            current_node = current_node.next
        if current_node is None:
            return
        # 最後のNodeに一致
        if current_node.next is None:
            prev_node = current_node.prev
            prev_node.next = None
            current_node = None
            return
        else:
            next_node = current_node.next
            prev_node = current_node.prev
            next_node.prev = prev_node
            prev_node.next = next_node
            current_node = None
            return

    def reverse(self):
        def _reverse(current_node: Node):
            if not current_node:
                return None

            prev_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = prev_node

            if current_node.prev is None:
                return current_node

            return _reverse(current_node.prev)

        self.head = _reverse(self.head)

    def sort(self):
        if self.head is None:
            return

        current_node = self.head
        while current_node.next:
            next_node = current_node.next
            while next_node:
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = next_node.data, current_node.data
                next_node = next_node.next
            current_node = current_node.next


l = LinkList()
l.insert(1)
l.append(2)
l.append(4)
l.remove(4)
l.print()
l.reverse()
l.print()
