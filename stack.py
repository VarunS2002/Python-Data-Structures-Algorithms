class Stack:
    class EmptyStackError(Exception):
        def __str__(self) -> str:
            return "Stack is empty."

    def __init__(self) -> None:
        self._data: list[object] = []
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def length(self) -> int:
        return self.__len__()

    def __str__(self) -> str:
        return str(self._data)

    def is_empty(self) -> bool:
        return self._size == 0

    def top(self) -> object:
        if self.is_empty():
            raise Stack.EmptyStackError
        return self._data[-1]

    def push(self, element: object) -> None:
        self._data.append(element)
        self._size += 1

    def pop(self) -> object:
        if self.is_empty():
            raise Stack.EmptyStackError
        self._size -= 1
        return self._data.pop()


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    for i in range(10):
        stack.push(i)
    print(stack.top())
    print(stack)
    print(len(stack))
    print(stack.length())
    print(stack.is_empty())
    for i in range(10):
        print(stack.pop())
    print(stack.is_empty())
