import numpy as np
import pandas as pd
from typing import Optional, List, Tuple, Dict, Any
from enum import Enum
import sys

class CellState(Enum):
    LIVING = True
    DEAD = False

class MapArray:
    def __init__(self):
        self.map_array: Optional[np.ndarray] = None
        self.num_rows: Optional[int] = None
        self.num_columns: Optional[int] = None

    def create_random_map(self, num_rows: int, num_columns: int, coverage:int) -> None:
        """
        Function creates a random map with the given inputs.

        Parameters:
            num_rows: (int) the number of rows of the map array
            num_columns: (int) the number of columns of the map array
            coverage: (int) the coverage of the map in percent (0-100)
        """
        random_ints = np.random.randint(0, 101, (num_rows, num_columns))
        random_map = np.where(random_ints <= coverage, CellState.LIVING, CellState.DEAD)

        self.num_rows = num_rows
        self.num_columns = num_columns
        self.map_array = random_map

    def create_given_map(self, input_list: list) -> None:
        """
        Function creates a map from a given input list.

        Parameters:
            input_list: (list) the list of input values corresponding
                to the map_array elements
        """
        input_map = np.array(input_list)
        self.map_array = np.where(input_map == 1, CellState.LIVING, CellState.DEAD)
        self.num_rows, self.num_columns = self.map_array.shape

    def state_on_point(self, row: int, column: int) -> CellState:
        """
        Function returns the current cell state at the given point

        Parameters:
            row: (int) the row to check
            column: (int) the column to check

        Returns:
            (CellState) the current state of the cell
        """
        return self.map_array[row][column]

    def living_neighbors(self, row: int, column: int) -> int:
        """
        Function returns the number of living cells around the given
        cell.

        Parameters:
             row: (int) the row to check
             column: (int) the column to check

        Returns:
            (int) the number of neighbours
        """
        offsets = [
            (row - 1, column - 1), (row - 1, column), (row - 1,column + 1),
            (row, column -1),           (row, column + 1),
            (row + 1, column - 1), (row + 1, column), (row + 1, column + 1)
        ]

        living_neighbors = 0

        for point in offsets:
            row, column = point
            if self.state_on_point(row, column) == CellState.LIVING:
                living_neighbors += 1

        return living_neighbors

    def print_map(self) -> None:
        living_symbol = '█'
        dead_symbol = '░'
        print("\033[H", end="")

        for row in self.map_array:
            row_str = ''.join(living_symbol if cell == CellState.LIVING else dead_symbol for cell in row)
            print(row_str)


if __name__ == '__main__':
    RandMap = MapArray()
    print(RandMap.create_random_map(5, 6, 90))

    given_list = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    GivenMap = MapArray()
    GivenMap.create_given_map(given_list)

    #print(GivenMap.state_on_point(2, 2))
    GivenMap.living_neighbors(2, 2)
    GivenMap.print_map()