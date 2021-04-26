from typing import Optional


class Node:
    def __init__(self, key: Optional[float]) -> None:
        self._left: Optional[Node] = None
        self._right: Optional[Node] = None
        self._value: Optional[float] = key

    def display(self) -> None:
        if self._left:
            self._left.display()
        print(self._value, end=' ')
        if self._right:
            self._right.display()

    def display_preorder(self) -> None:
        if self._value:
            print(self._value, end=' ')
            if self._left:
                self._left.display_preorder()
            if self._right:
                self._right.display_preorder()

    def display_inorder(self) -> None:
        if self._value:
            if self._left:
                self._left.display_inorder()
            print(self._value, end=' ')
            if self._right:
                self._right.display_inorder()

    def display_postorder(self) -> None:
        if self._value:
            if self._left:
                self._left.display_postorder()
            if self._right:
                self._right.display_postorder()
            print(self._value, end=' ')

    def insert(self, data: float) -> None:
        if self._value:
            if data < self._value:
                if self._left is None:
                    self._left = Node(data)
                else:
                    self._left.insert(data)
            elif data > self._value:
                if self._right is None:
                    self._right = Node(data)
                else:
                    self._right.insert(data)
        else:
            self._value = data


if __name__ == '__main__':
    root = Node(10)
    root._left = Node(12)
    root._right = Node(5)
    print("Without any order")
    root.display()
    print()
    root_1 = Node(None)
    root_1.insert(28)
    root_1.insert(4)
    root_1.insert(13)
    root_1.insert(130)
    root_1.insert(123)
    print("Now ordering with insert")
    root_1.display()
    print()
    print("Pre order")
    root_1.display_preorder()
    print()
    print("In Order")
    root_1.display_inorder()
    print()
    print("Post Order")
    root_1.display_postorder()
    print()
