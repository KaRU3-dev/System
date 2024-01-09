"""
平行四辺形
"""

import math
from Maijin.Math.plane import triangle

def area(w: float=0, h: float=0):
    return w * h

def cal_side_triangle_area(h: float=0, t: float=0):
    """
    Calculate side trianlge
    h (float): height
    t (float): theta
    @return (float): area
    """
    # Calculate side triangle's bottom
    w = h / math.tan(t)
    # Calculate side triangle's area
    a = triangle.area(w, h)
    # Return
    return a

def cal_side_triangle_l(w: float=0, h: float=0):
    """
    Calculate side triangle
    w (float): width
    h (float): height
    @return (float): long side
    """
    # Calculate side triangle's long side
    l = triangle.cal_l(w, h)
    return l

def cal_side_triangle_hypotenuse(w: float=0, h: float=0):
    """
    Calculate side triangle
    w (float): width
    h (float): height
    @return (float): hypotenuse
    """
    # Calculate side triangle's long side
    l = triangle.sidereal_length(w, h)
    return l
