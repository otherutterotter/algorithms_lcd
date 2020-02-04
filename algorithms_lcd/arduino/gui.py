import random
from tkinter import Tk, Label, Button, StringVar, OptionMenu
from algorithms_lcd.sorting.list import SortedList

"""
    ### GUI
    > algorithms_lcd.arduino.gui.GUI

    Tkinter GUI taking Board reference algorithms dictionary, number of items and list of type SortedList as arguments. 
    Algorithms dictionary keys will be visible as options and choosing them will trigger according function.
    Static method `run(board, algorithms, number_of_items, sorted_list)` creates and open GUI in selected setting.

    ```python
    gui = GUI(
      root, 
      {"merge_sort": print}, 
      10, 
      [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    )
    ```
"""


class GUI:
    def __init__(self, master, board, algorithms, n=10, sorted_list=SortedList([])):
        master.title("Algorithms LCD")
        padding = 10
        button_width = 20
        self.master = master
        self.board = board
        self.algorithms = algorithms
        self.n = n
        self.sorted_list = sorted_list
        random.shuffle(self.sorted_list)
        self.algorithm = StringVar()
        self.algorithm.set(list(algorithms.keys())[0])
        self.data_str = StringVar()
        self.data_str.set("".join(sorted_list))

        data_label = Label(self.master, textvariable=self.data_str, padx=padding, pady=padding)
        data_label.pack(padx=padding, pady=padding)

        algorithm_options = []
        for algorithm in algorithms.keys():
            algorithm_options.append(algorithm)
        algorithm_options_menu = OptionMenu(master, self.algorithm, *(algorithm_options))
        algorithm_options_menu.config(width=button_width)
        algorithm_options_menu.pack(padx=padding, pady=padding)

        generate_button = Button(master, text="Roll", command=self.roll_data, width=button_width)
        generate_button.pack(padx=padding)

        run_button = Button(master, text="Run", command=self.run_algorithm, width=button_width)
        run_button.pack(padx=padding, pady=padding)

    def run_algorithm(self):
        self.algorithms[self.algorithm.get()].sort(self.sorted_list)
        self.board.print_2d_data(self.algorithms[self.algorithm.get()].steps, self)
        self.data_str.set("".join(self.algorithms[self.algorithm.get()].sorted_list))

    def roll_data(self):
        random.shuffle(self.sorted_list)
        self.data_str.set("".join(self.sorted_list))

    def set_data_str(self, string):
        self.data_str.set(string)

    @staticmethod
    def run(board, algorithms, number_of_items, sorted_list):
        root = Tk()
        gui = GUI(root, board, algorithms, number_of_items, sorted_list)
        root.mainloop()



