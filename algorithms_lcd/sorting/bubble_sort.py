from algorithms_lcd.sorting.sorted_list import SortedList


def algorithm(sorted_list):
    """
    >>> sorted_list = SortedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    >>> algorithm(sorted_list)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    # sorted_list.add_step([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    sorted_list.swap_index(0, 1)
    sorted_list.add_step([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], True)
    sorted_list.swap_index(0, 1)
    # sorted_list.sort()

    return sorted_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()
