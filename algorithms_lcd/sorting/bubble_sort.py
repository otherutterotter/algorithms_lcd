from algorithms_lcd.sorting.sorted_data import SortedData


def algorithm(sorted_data):
    """
    >>> algorithm(data)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    sorted_data.swap_index(0, 1)
    sorted_data.sort()

    return sorted_data


if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={
        'data': SortedData([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    })
