"""
長方形
"""

from Maijin.Math.plane import triangle

def area(w: float=0, h: float=0):
    return w * h

def sidereal_length(w: float=0, h: float=0):
    return (w * 2) + (h * 2)

def cal_hypotenuse(w: float=0, h: float=0):
    return triangle.cal_l(w, h)
