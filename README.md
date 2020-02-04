# Algorithms-LCD
Arduino based interface for displaying step-by-step execution of specified sorting algorithm on an LCD screen. Project is based on Python and Firmata.

## Stack
- Arduino Uno (StandardFirmata template)
- Python 3.6

## Documentation
### Sort
> algorithms_lcd.sorting.algorithms.Sort

Class bundles sorting-related logic and tracks changes to the data during the execution of the algorithm. 

```python
bubble_sort = Sort(Sort.bubble_sort_algorithm)
bubble_sort.sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
bubble_sort.sorted_list
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

#### Parameters:
- `algorithm`:
    > Function for sorting data, which takes SortedList reference as an argument.
    > It should update SortedList which each successful swap to get the right number and values of steps
    > using such functions as push, pull, swap_index and swap_item on the SortedList instance.
    > It should also make a shallow object of the input list if there could be unnecessary updates on sorted_list.
    > Static methods available on the Sort prototype as an argument for algorithm are:
    - `bubble_sort_algorithm(sorted_list)`
    - `insertion_sort_algorithm(sorted_list)`
    - `merge_sort_algorithm(sorted_list)`
    - `quick_sort_algorithm(sorted_list)`

#### Available methods:
- `sort(data)`:
  Calls the sorting algorithm and using SortedList stores all the intermediate values inside the `self.steps`.

#### Notes:
- Using `print` function on the Sort instance outputs it's algorithm name and all the steps from the last sorting.

---

### SortedList
> algorithms_lcd.sorting.list.SortedList

Type extended from the List to record swaps needed to sort the list.

```python
sorted_list = SortedList([])
sorted_list.push(1)
sorted_list.replace(1,2)
sorted_list.push(3)
sorted_list.swap_item(3,2)
sorted_list.steps
# [[], [1], [2], [2, 3], [3, 2]]
```

#### Parameters:
- `list`:
  Initial data of the algorithm, which is also pushed to `self.steps` as a first member.

#### Available methods:
- `get_steps_len()`:
    Retrieves the length of the steps (with the initial step subtracted).
- `swapIndex(i1, i2)`:
    Swaps indexed items in the list and pushes its current state to the `self.steps`.
- `swapItem(item1, item2)`:
    Same as above, only items are referenced instead of indexes.
- `push(item)`: 
    Adds value to the list and pushes its current state to the `self.steps`.
- `pull(item)`: 
    Same as above, only item is removed instead.

#### Notes:
- Except for the methods above SortedList behaves like an ordinary list.

---

### GUI
> algorithms_lcd.arduino.gui.GUI

Tkinter GUI taking algorithms dictionary, number of items and list of type SortedList as arguments. 
Algorithms dictionary keys will be visible as options and choosing them will trigger according function
Static method `run(algorithms, number_of_items, sorted_list)` creates and open GUI in selected setting.

```python
gui = GUI(
  root, 
  {"merge_sort": print}, 
  10, 
  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
)
```

## Sources
- [The Hitchhikers Guide to Packaging](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html)
- [Arduino with Python](https://realpython.com/arduino-python/#arduino-software)
