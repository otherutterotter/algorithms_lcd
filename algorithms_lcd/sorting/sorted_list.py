import copy
"""
    ## SortedList
        Type extended from the List to store the history of swaps needed to sort the list.
    ### Parameters:
    - `list`:
        Initial data of the algorithm, which is also pushed to `self.steps` as a first member.
    ### Available methods:
    - `get_steps_len()`:
        Retrieves the length of the steps (with the initial step subtracted).
    - `swapIndex(i1, i2)`:
        Swaps indexed items in the list and pushes its current state to the `self.steps`.
    - `swapItem(item1, item2)`:
        Same as above, only items are referenced instead of indexes.
    - `push(item)`: 
        Adds value to the list and pushes its current state to the `self.steps`.
    - `pull(item)`: 
        Same as above, only item is removed instead.
    ### Notes:
    - Except for the methods above SortedList behaves like an ordinary list.
"""

class SortedList(list):
    def __init__(self, l):
        list.__init__(self, l)
        self.steps = [copy.copy(self)]

    def add_step(self, step, merge=False):
        self.steps.append(step)
        if merge:
            self.clear()
            for value in step:
                self.append(value)

    def swap_index(self, i1, i2):
        """
        >>> sorted_list = SortedList([0, 1])
        >>> sorted_list
        [0, 1]
        >>> sorted_list.swap_index(0, 1)
        >>> sorted_list
        [1, 0]
        >>> sorted_list.steps
        [[0, 1], [1, 0]]
        """
        tmp = self[i1]
        self[i1] = self[i2]
        self[i2] = tmp
        self.steps.append(copy.copy(self))

    def swap_item(self, item1, item2):
        i1 = self.index(item1)
        i2 = self.index(item2)
        self.swap_index(i1, i2)

    def push(self, item):
        """
        >>> sorted_list = SortedList([])
        >>> sorted_list.push('')
        >>> sorted_list.remove('')
        >>> len(sorted_list)
        0
        >>> len(sorted_list.steps)
        2
        """
        self.append(item)
        self.steps.append(copy.copy(self))

    def pull(self, item):
        """
        >>> sorted_list = SortedList([])
        >>> sorted_list.append('')
        >>> sorted_list.pull('')
        >>> len(sorted_list)
        0
        >>> len(sorted_list.steps)
        2
        """
        self.remove(item)
        self.steps.append(copy.copy(self))

    def get_steps_len(self):
        return len(self.steps) - 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()