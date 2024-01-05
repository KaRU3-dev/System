"""
Calculates the vector between two points
"""

import math

def cal(under: float=0, height: float=0, length: float=0):
    if under == 0 and height == 0 and length == 0:
        raise ValueError("All parameters cannot be zero")
    elif length == 0:
        return math.sqrt(under ** 2 + height ** 2)
    elif under == 0:
        return math.sqrt(length ** 2 + height ** 2)
    elif height == 0:
        return math.sqrt(length ** 2 + under ** 2)
    else:
        return math.sqrt(length ** 2 + under ** 2 + height ** 2)
