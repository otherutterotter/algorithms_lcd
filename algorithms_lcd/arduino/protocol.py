import sys
import time
from pyfirmata import Arduino, util, STRING_DATA
from serial.serialutil import SerialException
"""
    ### Board
    > algorithms_lcd.arduino.protocol.Board

    Class for accessing Arduino/lcd related methods. Contains only two functions: `print(string)` and 
    `print_2d_data(string)`, which render required result on the connected display. 
    Takes Arduino port and welcome string as arguments.
    
    ```python
    board = Board('COM3')
    ```
"""

TIME_LAG = 0.2


class Board:
    def __init__(self, port, hello_msg="hello, world!"):
        try:
            self.board = Arduino(port)
            self.print(hello_msg)
        except SerialException:
            print("Error: couldn't open port " + port)

    def print(self, text, gui=False):
        try:
            if text:
                if gui:
                    gui.set_data_str(text)
                self.board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(text))
        except TypeError:
            self.board.send_sysex(STRING_DATA, util.str_to_two_byte_iter('Error'))

    def print_2d_data(self, data, gui):
        for row in data:
            time.sleep(TIME_LAG)
            self.print("".join(row), gui)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        board = Board(sys.argv[1])
    else:
        print("You must provide port value as an argument")
