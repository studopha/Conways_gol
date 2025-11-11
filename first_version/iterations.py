import numpy as np
import pandas as pd
from typing import Optional, List, Tuple, Dict, Any
from enum import Enum
import time
import sys

from map_array.map_creation import MapArray, CellState
from setup.rule_set import check_second_rule, check_first_rule

def next_generation(map_array: MapArray) -> MapArray: # Rand gucken wahrscheinlich dead zone


    def dead_columns(num_columns: int) -> list:
        return [CellState.DEAD.value for column in range(num_columns)]

    dead_zone_columns = dead_columns(map_array.num_columns)

    next_gen_map = [dead_zone_columns]
    for row in range(1, map_array.num_rows - 1):
        row_builder = [CellState.DEAD.value]
        for column in range(1, map_array.num_columns- 1):
            if map_array.state_on_point(row, column) == CellState.LIVING:
                if check_first_rule(map_array, row, column):
                    row_builder.append(CellState.LIVING.value)
                else:
                    row_builder.append(CellState.DEAD.value)
            else:
                if check_second_rule(map_array, row, column):
                    row_builder.append(CellState.LIVING.value)
                else:
                    row_builder.append(CellState.DEAD.value)
        row_builder.append(CellState.DEAD.value)
        next_gen_map.append(row_builder)
    next_gen_map.append(dead_zone_columns)

    map_array.create_given_map(next_gen_map)
    map_array.print_map()
    return map_array


if __name__ == '__main__':
    given_list = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    GivenMap = MapArray()
    GivenMap.create_given_map(given_list)

    next_generation(GivenMap)


    for i in range(20):
        GivenMap = next_generation(GivenMap)
        time.sleep(0.1)
