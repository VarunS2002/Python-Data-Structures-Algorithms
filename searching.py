from typing import Union

from sorting import Sorting


class Searching:
    @staticmethod
    def linear_search(list_to_search: list[object], element: object) -> Union[int, bool]:
        for i in range(len(list_to_search)):
            if list_to_search[i] == element:
                return i
        return False

    @staticmethod
    def binary_search(list_to_search: list[float], element: float) -> Union[int, bool]:
        sorted_lst: list[float] = Sorting.merge_sort(list_to_search)
        start: int = 0
        end: int = len(sorted_lst) - 1
        while start <= end:
            mid: int = (end + start) // 2
            if sorted_lst[mid] < element:
                start = mid + 1
            elif sorted_lst[mid] > element:
                end = mid - 1
            else:
                return mid
        return False


if __name__ == '__main__':
    test_list = [35, 10, 43, 82, 66, 51, 97]
    test_list_2 = [44, 11, 36, 52, 67, 83, 98]
    test_value_1 = 43
    test_value_2 = 44
    binary_result_1 = Searching.binary_search(test_list, test_value_1)
    print(binary_result_1)
    binary_result_2 = Searching.binary_search(test_list_2, test_value_2)
    print(binary_result_2)
    linear_result_1 = Searching.linear_search(test_list, test_value_1)
    print(linear_result_1)
    linear_result_2 = Searching.linear_search(test_list_2, test_value_2)
    print(linear_result_2)
