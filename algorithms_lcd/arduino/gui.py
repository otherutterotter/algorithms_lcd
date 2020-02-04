import random
from tkinter import Tk, Label, Button, StringVar, OptionMenu
from algorithms_lcd.sorting.list import SortedList

"""
    ### GUI
    > algorithms_lcd.arduino.gui.GUI

    Tkinter GUI taking algorithms dictionary, number of items and list of type SortedList as arguments. 
    Algorithms dictionary keys will be visible as options and choosing them will trigger according function.
    Static method `run(algorithms, number_of_items, sorted_list)` creates and open GUI in selected setting.

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
    def __init__(self, master, algorithms, n=10, sorted_list=SortedList(['9', '8', '7', '6', '5', '4', '3', '2', '1'])):
        master.title("Algorithms LCD")
        padding = 10
        button_width = 20
        self.master = master
        self.algorithms = algorithms
        self.n = n
        self.sorted_list = sorted_list
        self.algorithm = StringVar()
        self.algorithm.set(list(algorithms.keys())[0])
        self.data_str = StringVar()
        self.data_str.set("".join(sorted_list))

        data_label = Label(self.master, textvariable=self.data_str, padx=padding, pady=padding)
        data_label.pack(padx=padding, pady=padding)

        algorithm_options = []
        for algorithm in algorithms.keys():
            algorithm_options.append(algorithm)
        print(algorithm_options)
        print(self.algorithm.get())
        algorithm_options_menu = OptionMenu(master, self.algorithm, *(algorithm_options))
        algorithm_options_menu.config(width=button_width)
        algorithm_options_menu.pack(padx=padding, pady=padding)

        generate_button = Button(master, text="Roll", command=self.roll_data, width=button_width)
        generate_button.pack(padx=padding)

        run_button = Button(master, text="Run", command=self.run_algorithm, width=button_width)
        run_button.pack(padx=padding, pady=padding)

    def run_algorithm(self):
        self.algorithms[self.algorithm.get()](self.sorted_list)

    def roll_data(self):
        data = []
        for i in range(self.n):
            data.append(str(int(random.random() * self.n)))
        self.sorted_list = SortedList(data)
        self.data_str.set("".join(self.sorted_list))

    @staticmethod
    def run(algorithms, number_of_items, sorted_list):
        root = Tk()
        gui = GUI(root, algorithms, number_of_items, sorted_list)
        root.mainloop()



