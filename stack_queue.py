class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()


"""
Input {'key1': 'value1', 'key2': [1, 2, 3], 'key3': (1, 2, 3)} -> True
Input {'key1': ['value1', 'key2': [1, 2, 3], 'key3': (1, 2, 3)} -> False
"""


def validate_format(chars: str) -> bool:
    lookup = {'{': '}', '(': ')', '[': ']'}
    stack = []
    for char in chars:
        if char in lookup.keys():
            stack.append(lookup[char])
        elif char in lookup.values():
            if not stack:
                return False
            if char != stack.pop():
                return False

    if stack:
        return False

    return True


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        """
        先頭から取り出す
        """
        self.queue.pop(0)

    def reverse(self):
        new_queue = []
        while self.queue:
            new_queue.append(self.queue.pop())
        self.queue = new_queue


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.reverse()
q.dequeue()
