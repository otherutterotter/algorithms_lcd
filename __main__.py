#!/usr/bin/env python
# from pyfirmata import Arduino, util, STRING_DATA
# board = Arduino(sys.argv[ 1]) # PORT, e.g. "COM3"
# board.send_sysex(STRING_DATA, util.str_to_two_byte_iter('Hello!'))
#
#
# def msg(text):
#   if text:
#     board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(text))

if __name__ == '__main__':
    from algorithms_lcd.sorting.algorithms import Sort
    DATA = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubble_sort = Sort(Sort.quick_sort_algorithm)
    bubble_sort.sort(DATA)
    print(bubble_sort)


