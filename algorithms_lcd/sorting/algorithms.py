import copy
from algorithms_lcd.sorting.sorted_data import SortedData
from algorithms_lcd.sorting import bubble_sort

"""
    ## Sort
        Class bundles sorting-related logic and tracks changes to the data during the execution of the algorithm. 
    ### Parameters:
    - `algorithm`:
        Function for sorting data, which takes 'self.sorted_data' reference as an argument.
        It should update sorted_data which each successful swap to get the right number and values of steps
        using such functions as push, pull, swap_index and swap_item.
        It should also make a shallow object of the input list if there could be unnecessary updates on sorted_data.
        Static methods available on the Sort prototype as an argument for algorithm are:
            - `bubble_sort_algorithm(data)`
    ### Available methods:
    - `sort`:
        Calls the sorting algorithm and using SortedData puts all the intermediate values inside the `self.steps`.
    ### Notes:
    - using `print` function on the Sort instance outputs it's algorithm name and all the steps from the last sorting
"""


class Sort:
    def __init__(self, algorithm):
        # shallow copy of the input data provided for sorting
        self.data = []
        self.algorithm = algorithm
        # instantiated as SortedData object during sort function execution
        self.sorted_data = []
        # takes value of sorted_data.steps
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
        >>> bubble_sort.sorted_data
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        >>> len(bubble_sort.steps) > 0
        True
        """
        self.data = data
        sorted_data = SortedData(data)
        self.algorithm(sorted_data)
        self.steps = sorted_data.steps
        self.sorted_data = copy.copy(sorted_data)

    @staticmethod
    def bubble_sort_algorithm(sorted_data):
        """
        >>> Sort.bubble_sort_algorithm(SortedData(data))
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        """
        return bubble_sort.algorithm(sorted_data)


"""
    ## SortedData
        Class extending list to track all the changes of its content inside the `self.steps` variable.
    ### Parameters:
    - `list`:
        Input list based on which SortedData is initialized.
    ### Available methods:
    - `add_step(list)`
        Appends whole step to the `self.steps`
    - `swap_index(number, number)`
        Swaps two items in the list based on their indexes and updates `self.steps`
    - `swap_item(item, item)`:
        Swaps two items in the list and updates `self.steps`
    - `push(item)`:
        Adds item to the list and updates `self.steps`
    - `pull(item)`:
        Removes item from the list and updates `self.steps`
"""


if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={
        'data': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        'bubble_sort': Sort(Sort.bubble_sort_algorithm),
    })
