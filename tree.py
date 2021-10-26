from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node: Node, value: int) -> Node:
            if node is None:
                return Node(value)

            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)

            return node

        _insert(self.root, value)

    def inorder(self):
        def _inorder(node: Node):
            """
            左にあるNodeから順にprint
            """
            if node is not None:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)

        _inorder(self.root)

    def search(self, value: int) -> bool:
        def _search(node: Optional[Node], value: int) -> bool:
            """
            指定したvalueが存在するかboolを返す
            """
            if node is None:
                return False

            if node.value == value:
                return True
            elif value < node.value:
                return _search(node.left, value)
            elif value > node.value:
                return _search(node.right, value)
            else:
                return False

        return _search(self.root, value)

    def remove(self, value: int):
        def _remove(node: Optional[Node], value: int) -> Optional[Node]:
            """
            指定したvalueを削除して、ツリー構造を作り直す
            """
            if node is None:
                return node

            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                # value配下が二股に別れてたとき
                temp = self._min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value)
            return node

        _remove(self.root, value)

    def _min_value(self, node: Node) -> Node:
        """
        ツリーの中で1番小さい値を返す
        """
        current = node
        while current.left:
            current = current.left
        return current


bst = BinarySearchTree()
bst.insert(5)
bst.insert(6)
bst.insert(3)
b = bst.search(3)
print(b)
bst.remove(5)
bst.inorder()
