import random
import time
from typing import Callable, Optional

import matplotlib.pyplot as plt

from sorting import Sorting


class SortingTimeComparison:
    def __init__(self, print_scores_to_console: bool = True, plot_graph: bool = True,
                 print_total_runtime_to_console: bool = True,
                 no_of_elements: Optional[list[int]] = None) -> None:
        self.__start_time: float = time.time()
        self.__no_of_elements: list[int] = no_of_elements
        if self.__no_of_elements is None:
            self.__no_of_elements = [
                250, 500, 3000,
                5000, 7000,
                10000, 15000, 20000,
                # 100000, 1000000
            ]
        self.__algorithms: list[list[float]] = [[], [], [], [], []]
        self.__legends: list[str] = ['Quick', 'Merge', 'Selection', 'Insertion', 'Bubble']
        self.__time_taken: list[dict[str, float]] = [
            {'quick_sort': 0, 'merge_sort': 0, 'selection_sort': 0, 'insertion_sort': 0, 'bubble_sort': 0}
            for _ in range(len(self.__no_of_elements))]
        self.__index: int = 0
        self.__run_algorithms()
        if plot_graph:
            self.plot_graph()
        if print_scores_to_console:
            self.print_scores()
        if print_total_runtime_to_console:
            print(f'Total Runtime: {time.time() - self.__start_time} seconds')

    def __timed_sort(self, sort: Callable[[list[float]], list[float]], unsorted_list: list[float]) -> list[float]:
        start: float = time.time()
        result: list[float] = sort(unsorted_list)
        duration: float = time.time() - start
        self.__time_taken[self.__index][str(sort.__name__)] = duration
        return result

    def __run_algorithms(self) -> None:
        for number in self.__no_of_elements:
            test_list: list[int] = [random.randint(-1000000, 1000000) for _ in range(number)]
            self.__timed_sort(Sorting.quick_sort, test_list)
            self.__timed_sort(Sorting.merge_sort, test_list)
            self.__timed_sort(Sorting.selection_sort, test_list)
            self.__timed_sort(Sorting.insertion_sort, test_list)
            self.__timed_sort(Sorting.bubble_sort, test_list)
            self.__index += 1
        self.__save_scores()

    def __save_scores(self) -> None:
        j: int = 0
        for dictionary in self.__time_taken:
            i: int = 0
            j += 1
            for key, value in dictionary.items():
                if i % 5 == 0:
                    i = 0
                self.__algorithms[i].append(value)
                i += 1

    def print_scores(self) -> None:
        j: int = 0
        for dictionary in self.__time_taken:
            i: int = 0
            print('Number of elements= ', self.__no_of_elements[j], end=' : ')
            j += 1
            for key, value in dictionary.items():
                if i % 5 == 0:
                    i = 0
                i += 1
                print(key.replace('_', ' ').capitalize(), ' : ', value, end=', ')
            print()

    def plot_graph(self) -> None:
        fig: plt.Figure = plt.figure()
        fig.add_subplot(1, 1, 1)
        plt.xlabel("Number of Elements")
        plt.ylabel("Time in Seconds")
        plt.plot(self.__no_of_elements, self.__algorithms[0], 'go-')
        plt.plot(self.__no_of_elements, self.__algorithms[1], 'co-')
        plt.plot(self.__no_of_elements, self.__algorithms[2], 'bo-')
        plt.plot(self.__no_of_elements, self.__algorithms[3], 'mo-')
        plt.plot(self.__no_of_elements, self.__algorithms[4], 'ro-')
        plt.legend(self.__legends)
        plt.show()


if __name__ == '__main__':
    sorting_time_comparison = SortingTimeComparison(print_scores_to_console=False, plot_graph=False)
    sorting_time_comparison.print_scores()
    sorting_time_comparison.plot_graph()
