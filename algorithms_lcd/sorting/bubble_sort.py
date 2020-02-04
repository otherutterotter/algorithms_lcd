from algorithms_lcd.sorting.sorted_list import SortedList


def algorithm(sorted_list):
    """
    >>> sorted_list = SortedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    >>> algorithm(sorted_list)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """

    length = len(sorted_list)
    n_of_swaps = length
    while n_of_swaps > 0:
        n_of_swaps = 0
        for i in range(length):
            if i < length - 1:
                first_item = sorted_list[i]
                second_item = sorted_list[i + 1]
                if first_item > second_item:
                    sorted_list.swap_item(first_item, second_item)
                    n_of_swaps += 1
    return sorted_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()
