import sys
import time
from pyfirmata import Arduino, util, STRING_DATA
from serial.serialutil import SerialException
"""
    ### Board
    > algorithms_lcd.arduino.protocol.Board

    Class for accessing Arduino/lcd related methods. Contains only two functions: `print(string)` and 
    `print_2d_data(string)`, which render required result on the connected display. Takes Arduino port as an argument.
    
    ```python
    board = Board('COM3')
    ```
"""


class Board:
    def __init__(self, port):
        try:
            self.board = Arduino(port)
        except SerialException:
            print("Error: couldn't open port " + port)

    def print(self, text, sleep_rate=0.8):
        try:
            if text:
                self.board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(text))
                time.sleep(sleep_rate)
        except TypeError:
            self.board.send_sysex(STRING_DATA, util.str_to_two_byte_iter('Error'))

    def print_2d_data(self, data):
        for row in data:
            self.print("".join(row))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        board = Board(sys.argv[1])
        board.print_2d_data([
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            ['1', '1', '1', '1', '1', '6', '7', '8', '9', '10']
        ])
    else:
        print("You must provide port value as an argument")
