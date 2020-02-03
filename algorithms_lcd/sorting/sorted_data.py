import copy


class SortedData(list):
    def __init__(self, l):
        list.__init__(self, l)
        self.steps = [copy.copy(self)]

    def add_step(self, step):
        self.steps.append(step)

    def swap_index(self, i1, i2):
        """
        >>> sorted_data = SortedData([0, 1])
        >>> sorted_data
        [0, 1]
        >>> sorted_data.swap_index(0, 1)
        >>> sorted_data
        [1, 0]
        >>> sorted_data.steps
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
        >>> sorted_data = SortedData([])
        >>> sorted_data.push('')
        >>> sorted_data.remove('')
        >>> len(sorted_data)
        0
        >>> len(sorted_data.steps)
        2
        """
        self.append(item)
        self.steps.append(copy.copy(self))

    def pull(self, item):
        """
        >>> sorted_data = SortedData([])
        >>> sorted_data.append('')
        >>> sorted_data.pull('')
        >>> len(sorted_data)
        0
        >>> len(sorted_data.steps)
        2
        """
        self.remove(item)
        self.steps.append(copy.copy(self))


if __name__ == '__main__':
    import doctest
    doctest.testmod()