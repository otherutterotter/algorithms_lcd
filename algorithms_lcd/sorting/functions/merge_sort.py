import copy
from algorithms_lcd.sorting.list import SortedList


def get_merge_sort_steps(sorted_list):
    steps = []
    for step in sorted_list.steps:
        if len(step) == len(sorted_list):
            steps.append(step)
    return steps


def algorithm(sorted_list, root_list_ref=False, steps=[]):
    """
    >>> sorted_list = SortedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    >>> algorithm(sorted_list)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """

    length = len(sorted_list)

    if length > 1:
        middle = length // 2
        left_half = SortedList(sorted_list[:middle])
        right_half = SortedList(sorted_list[middle:])

        algorithm(left_half, sorted_list)
        algorithm(right_half, sorted_list)

        i = j = k = 0
        left_half_length = len(left_half)
        right_half_length = len(right_half)

        while i < left_half_length and j < right_half_length:
            if left_half[i] < right_half[j]:
                sorted_list[k] = left_half[i]
                steps.append(copy.copy(sorted_list))
                i += 1
            else:
                sorted_list[k] = right_half[j]
                steps.append(copy.copy(sorted_list))
                j += 1
            k += 1

        while i < left_half_length:
            sorted_list[k] = left_half[i]
            steps.append(copy.copy(sorted_list))
            i += 1
            k += 1

        while j < right_half_length:
            sorted_list[k] = right_half[j]
            steps.append(copy.copy(sorted_list))
            j += 1
            k += 1
    if root_list_ref:
        root_list_ref.steps = steps
        root_list_ref.steps = get_merge_sort_steps(sorted_list)
    else:
        sorted_list.steps = steps
        sorted_list.steps = get_merge_sort_steps(sorted_list)

    return sorted_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()
