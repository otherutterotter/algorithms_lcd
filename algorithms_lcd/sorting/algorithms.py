import copy
from algorithms_lcd.sorting.sorted_list import SortedList
from algorithms_lcd.sorting import bubble_sort
"""
    ## Sort
        Class bundles sorting-related logic and tracks changes to the data during the execution of the algorithm. 
    ### Parameters:
    - `algorithm`:
        Function for sorting data, which takes SortedList reference as an argument.
        It should update SortedList which each successful swap to get the right number and values of steps
        using such functions as push, pull, swap_index and swap_item on the SortedList instance.
        It should also make a shallow object of the input list if there could be unnecessary updates on sorted_list.
        Static methods available on the Sort prototype as an argument for algorithm are:
            - `bubble_sort_algorithm(data)`
    ### Available methods:
    - `sort(data)`:
        Calls the sorting algorithm and using SortedList stores all the intermediate values inside the `self.steps`.
    ### Notes:
    - Using `print` function on the Sort instance outputs it's algorithm name and all the steps from the last sorting.
"""


class Sort:
    def __init__(self, algorithm):
        # shallow copy of the input data provided for sorting
        self.data = []
        self.algorithm = algorithm
        # instantiated as SortedList object during sort function execution
        self.sorted_list = []
        # takes value of sorted_list.steps
        self.steps = []

    def __str__(self):
        steps_str = ''
        for step in self.steps:
            steps_str_row = '\n['
            for val in step:
                if step.index(val) == len(step) - 1:
                    steps_str_row += str(val)
                else:
                    steps_str_row += str(val) + ','
            steps_str_row += ']'
            steps_str += steps_str_row
        return '\n' + self.algorithm.__name__ + steps_str

    def sort(self, data):
        """
        >>> bubble_sort.sort(data)
        >>> bubble_sort.sorted_list
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        >>> len(bubble_sort.steps) > 0
        True
        """
        self.data = data
        sorted_list = SortedList(data)
        self.algorithm(sorted_list)
        self.steps = sorted_list.steps
        self.sorted_list = copy.copy(sorted_list)

    @staticmethod
    def bubble_sort_algorithm(sorted_list):
        """
        >>> Sort.bubble_sort_algorithm(SortedList(data))
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        """
        return bubble_sort.algorithm(sorted_list)


if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={
        'data': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        'bubble_sort': Sort(Sort.bubble_sort_algorithm),
    })
