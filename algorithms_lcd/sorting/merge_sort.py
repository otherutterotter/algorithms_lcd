import copy
from algorithms_lcd.sorting.sorted_list import SortedList


def algorithm(sorted_list, root_list_ref):
    # """
    # >>> sorted_list = SortedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    # >>> algorithm(sorted_list)
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # """

    length = len(sorted_list)
    original_length = len(root_list_ref)

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
                # if length == original_length:
                # root_list_ref.add_step(copy.copy(sorted_list))
                # sorted_list.replace(sorted_list[k], left_half[i])
                i += 1
            else:
                sorted_list[k] = right_half[j]
                # root_list_ref.add_step(copy.copy(sorted_list))
                # sorted_list.replace(sorted_list[k], right_half[i])
                j += 1
            k += 1
            root_list_ref.add_step(copy.copy(sorted_list))

        while i < left_half_length:
            sorted_list[k] = left_half[i]
            # root_list_ref.add_step(copy.copy(sorted_list))
            # sorted_list.replace(sorted_list[k], left_half[i])
            i += 1
            k += 1

        while j < right_half_length:
            sorted_list[k] = right_half[j]
            # root_list_ref.add_step(copy.copy(sorted_list))
            # sorted_list.replace(sorted_list[k], right_half[i])
            j += 1
            k += 1
        root_list_ref.add_step(copy.copy(sorted_list))

    # for step in sorted_list.steps:
    #     print(step)
    # root_list_ref.add_step(copy.copy(sorted_list))
    return sorted_list


if __name__ == '__main__':
    sorted_list1 = SortedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    algorithm(sorted_list1, sorted_list1)
    print(sorted_list1.steps)
    print(sorted_list1)

    # import doctest
    # doctest.testmod()
