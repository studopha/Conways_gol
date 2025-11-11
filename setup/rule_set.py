import numpy as np
import pandas as pd
from typing import Optional, List, Tuple, Dict, Any
from enum import Enum

from map_array.map_creation import MapArray
#1. Eine lebende Zelle lebt auch in der Folgegeneration, wenn sie entweder zwei oder drei lebende Nachbarn hat.
#Im Beispiel hat die lebende mittlere Zelle genau zwei lebende Nachbarn und wird in der nächsten Generation weiterhin
# leben. Über die anderen Zellen lässt sich ohne Kenntnis ihrer weiteren Nachbarn keine Aussage machen

def check_first_rule(map_array: MapArray, row: int, column: int) -> bool:
    """
    Checks if the cell lives in the next generation and returns true if it does. False otherwise.
    It survives if the cell has 2 or 3 living cells next to it.

    Parameters:
        map_array: (MapArray) the map instance
        row: (int) the current row
        column: (int) the current column

    Returns:
        (bool) True if the rule is fulfilled, False otherwise
    """
    living_neighbors = map_array.living_neighbors(row, column)

    if living_neighbors in [2, 3]:
        return True
    else:
        return False


#2. Eine tote Zelle „wird geboren“ (lebt in der Folgegeneration), wenn sie genau drei lebende Nachbarn hat.
#Im Beispiel hat die tote mittlere Zelle genau drei lebende Nachbarn und wird in der nächsten Generation leben.


def check_second_rule(map_array: MapArray, row: int, column: int) -> bool:
    """
    Checks if the gets born in the next generation and returns true if it does. False otherwise.
    It gets born if it has exactly 3 neighboring cells that live.

    Parameters:
        map_array: (MapArray) the map instance
        row: (int) the current row
        column: (int) the current column

    Returns:
        (bool) True if the rule is fulfilled, False otherwise
    """
    living_neighbors = map_array.living_neighbors(row, column)

    if living_neighbors == 3:
        return True
    else:
        return False