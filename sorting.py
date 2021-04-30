from typing import Optional


class Sorting:
    @staticmethod
    def quick_sort(unsorted_list: list[float]) -> list[float]:
        sorted_list: list[float] = unsorted_list.copy()
        Sorting.__quick_sort_implementation(sorted_list)
        return sorted_list

    @staticmethod
    def __quick_sort_implementation(unsorted_list: list[float], low: Optional[int] = None,
                                    high: Optional[int] = None) -> list[float]:
        if low is None and high is None:
            low = 0
            high = len(unsorted_list) - 1

        def partition(p_list: list[float], p_low: int, p_high: int) -> int:
            i: int = p_low - 1
            pivot: float = p_list[p_high]
            for j in range(p_low, p_high):
                if p_list[j] <= pivot:
                    i += 1
                    p_list[i], p_list[j] = p_list[j], p_list[i]
            p_list[i + 1], p_list[p_high] = p_list[p_high], p_list[i + 1]
            return i + 1

        if len(unsorted_list) == 1:
            return unsorted_list
        if low < high:
            p_i: int = partition(unsorted_list, low, high)
            Sorting.__quick_sort_implementation(unsorted_list, low=low, high=p_i - 1)
            Sorting.__quick_sort_implementation(unsorted_list, low=p_i + 1, high=high)

    @staticmethod
    def merge_sort(unsorted_list: list[float]) -> list[float]:
        sorted_list: list[float] = unsorted_list.copy()
        if len(sorted_list) > 1:
            mid: int = len(sorted_list) // 2
            left: list[float] = Sorting.merge_sort(sorted_list[:mid])
            right: list[float] = Sorting.merge_sort(sorted_list[mid:])
            i: int = 0
            j: int = 0
            k: int = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_list[k] = left[i]
                    i += 1
                else:
                    sorted_list[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                sorted_list[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                sorted_list[k] = right[j]
                j += 1
                k += 1
        return sorted_list

    @staticmethod
    def selection_sort(unsorted_list: list[float]) -> list[float]:
        sorted_list: list[float] = unsorted_list.copy()
        for i in range(len(sorted_list)):
            min_idx: int = i
            for j in range(i + 1, len(sorted_list)):
                if sorted_list[min_idx] > sorted_list[j]:
                    min_idx = j
            sorted_list[i], sorted_list[min_idx] = sorted_list[min_idx], sorted_list[i]
        return sorted_list

    @staticmethod
    def insertion_sort(unsorted_list: list[float]) -> list[float]:
        sorted_list: list[float] = unsorted_list.copy()
        for i in range(1, len(sorted_list)):
            key: float = sorted_list[i]
            j: int = i - 1
            while j >= 0 and key < sorted_list[j]:
                sorted_list[j + 1] = sorted_list[j]
                j -= 1
            sorted_list[j + 1] = key
        return sorted_list

    @staticmethod
    def bubble_sort(unsorted_list: list[float]) -> list[float]:
        sorted_list: list[float] = unsorted_list.copy()
        for i in range(len(sorted_list) - 1):
            for j in range(0, len(sorted_list) - i - 1):
                if sorted_list[j] > sorted_list[j + 1]:
                    sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
        return sorted_list


if __name__ == '__main__':
    array = [9, 100.55, 100.46, 8, 1, 9999, 5]
    print("Before:", array)
    print("Quick:", Sorting.quick_sort(array))
    print("Merge:", Sorting.merge_sort(array))
    print("Selection:", Sorting.selection_sort(array))
    print("Insertion:", Sorting.insertion_sort(array))
    print("Bubble:", Sorting.bubble_sort(array))
    print("After:", array)
