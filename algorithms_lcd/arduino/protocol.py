from pyfirmata import Arduino, util, STRING_DATA
from serial.serialutil import SerialException


class Board:
    def __init__(self, port):
        try:
            self.board = Arduino(port)
            self.print('Hello!')
        except SerialException:
            print("Error: couldn't open port " + port)

    def print(self, text):
        if text:
            self.board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(text))
