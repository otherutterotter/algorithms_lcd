from algorithms_lcd.sorting.list import SortedList


def partition(sorted_list, low, high):
    i = (low - 1)
    pivot = sorted_list[high]

    for j in range(low, high):
        if sorted_list[j] < pivot:
            i = i + 1
            sorted_list.swap_index(i, j)

    sorted_list.swap_index(i + 1, high)
    return i + 1


def algorithm(sorted_list, low, high):
    """
    >>> sorted_list = SortedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    >>> algorithm(sorted_list)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """

    if low < high:
        # pi is partitioning index, sorted_list[p] is now
        # at right place
        pi = partition(sorted_list, low, high)

        # Separately sort elements before
        # partition and after partition
        algorithm(sorted_list, low, pi - 1)
        algorithm(sorted_list, pi + 1, high)

    return sorted_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()
