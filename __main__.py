#!/usr/bin/env python
import sys
from algorithms_lcd.sorting.algorithms import Sort
from algorithms_lcd.arduino.protocol import Board

if __name__ == '__main__':
    if len(sys.argv) > 1:
        board = Board(sys.argv[1])
    else:
        DATA = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        bubble_sort = Sort(Sort.quick_sort_algorithm)
        bubble_sort.sort(DATA)
        print(bubble_sort)


