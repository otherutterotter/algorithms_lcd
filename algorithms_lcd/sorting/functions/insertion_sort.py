from algorithms_lcd.sorting.list import SortedList


def algorithm(sorted_list):
    """
    >>> sorted_list = SortedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    >>> algorithm(sorted_list)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """

    length = len(sorted_list)

    for i in range(1, length):
        key = sorted_list[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < sorted_list[j]:
            sorted_list.swap_item(sorted_list[j], sorted_list[j + 1])
            j -= 1
        sorted_list.swap_item(sorted_list[j + 1], key)
    return sorted_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()
