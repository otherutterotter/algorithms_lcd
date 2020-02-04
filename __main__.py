#!/usr/bin/env python
import sys
from algorithms_lcd.sorting.algorithms import Sort
from algorithms_lcd.sorting.list import SortedList
from algorithms_lcd.arduino.gui import GUI
from algorithms_lcd.arduino.protocol import Board

if __name__ == '__main__':
    DATA = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(sys.argv) > 1:
        board = Board(sys.argv[1], "Algorithms LCD")
        bubble_sort = Sort(Sort.bubble_sort_algorithm)
        insertion_sort = Sort(Sort.insertion_sort_algorithm)
        merge_sort = Sort(Sort.merge_sort_algorithm)
        quick_sort = Sort(Sort.quick_sort_algorithm)

        GUI.run(board, {
            "insertion sort": insertion_sort,
            "merge_sort": merge_sort,
            "quick_sort": quick_sort,
            "bubble sort": bubble_sort
        }, 9, SortedList(DATA))

    else:
        bubble_sort = Sort(Sort.merge_sort_algorithm)
        bubble_sort.sort(DATA)
        print(bubble_sort)


