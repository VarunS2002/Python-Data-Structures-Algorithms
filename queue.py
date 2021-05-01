from typing import Optional


class _BaseQueue:
    class _EmptyQueueError(Exception):
        def __str__(self) -> str:
            return "Queue is empty."

    def __init__(self) -> None:
        self._data: list[Optional[object]] = [None] * 10
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def length(self) -> int:
        return self.__len__()

    def __str__(self) -> str:
        return str(self._data)

    def is_empty(self) -> bool:
        return self._size == 0


class SingleEndedQueue(_BaseQueue):
    def __init__(self) -> None:
        super().__init__()
        self._front: int = 0

    def __eq__(self, other: 'SingleEndedQueue') -> bool:
        if self.__class__ == other.__class__:
            if self._data == other._data and self._front == other._front:
                return True
        return False

    def first(self) -> Optional[object]:
        if self.is_empty():
            raise self._EmptyQueueError
        return self._data[self._front]

    def _resize(self, capacity: int) -> None:
        old: list[Optional[object]] = self._data
        self._data = [None] * capacity
        walk: int = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def enqueue_back(self, element: Optional[object]) -> None:
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail: int = (self._front + self._size) % len(self._data)
        self._data[avail] = element
        self._size += 1

    def dequeue_front(self) -> Optional[object]:
        if self.is_empty():
            raise self._EmptyQueueError
        element: Optional[object] = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return element


class DoubleEndedQueue(SingleEndedQueue):
    def __init__(self) -> None:
        super().__init__()
        self._back = 0

    def __eq__(self, other: 'DoubleEndedQueue') -> bool:
        if self.__class__ == other.__class__:
            if self._data == other._data and self._front == other._front and self._back == other._back:
                return True
        return False

    def last(self) -> Optional[object]:
        if self.is_empty():
            raise self._EmptyQueueError
        return self._data[self._back]

    def _resize(self, capacity: int) -> None:
        super(DoubleEndedQueue, self)._resize(capacity)
        self._back = (self._front + self._size - 1) % len(self._data)

    def enqueue_back(self, element: Optional[object]) -> None:
        super(DoubleEndedQueue, self).enqueue_back(element)
        self._back = (self._front + self._size - 1) % len(self._data)

    def dequeue_front(self) -> Optional[object]:
        element: Optional[object] = super(DoubleEndedQueue, self).dequeue_front()
        self._back = (self._front + self._size - 1) % len(self._data)
        return element

    def enqueue_front(self, element: Optional[object]) -> None:
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = element
        self._size += 1
        self._back = (self._front + self._size - 1) % len(self._data)

    def dequeue_back(self) -> Optional[object]:
        if self.is_empty():
            raise self._EmptyQueueError
        back: int = (self._front + self._size - 1) % len(self._data)
        element: Optional[object] = self._data[back]
        self._data[back] = None
        self._size -= 1
        self._back = (self._front + self._size - 1) % len(self._data)
        return element


if __name__ == '__main__':
    print("1. Single Ended Queue")
    print("2. Double Ended Queue")
    mode = int(input("Choose:"))
    if mode == 1:
        single_ended_queue = SingleEndedQueue()
        for i in range(1, 11):
            single_ended_queue.enqueue_back("f_" + str(i))
        print(single_ended_queue.first())
        print(single_ended_queue.dequeue_front())
        single_ended_queue.enqueue_back("f_" + str(11))
        print(single_ended_queue.first())
        print(single_ended_queue)
    elif mode == 2:
        double_ended_queue = DoubleEndedQueue()
        for i in range(1, 6):
            double_ended_queue.enqueue_back("f_" + str(i))
        print(double_ended_queue.first())
        print(double_ended_queue.dequeue_front())
        double_ended_queue.enqueue_front("f_" + str(1))
        print(double_ended_queue.first())
        print(double_ended_queue.last())
        print(double_ended_queue.dequeue_back())
        print(double_ended_queue.last())
