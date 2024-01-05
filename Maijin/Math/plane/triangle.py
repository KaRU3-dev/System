"""
三角形
"""

from math import sqrt

def area(w: float=0, h: float=0):
    return w * h / 2

def sidereal_length(w: float=0, h: float=0):
    l = cal_l(w, h)
    return w + h + l

def cal_l(w: float=0, h: float=0):
    return sqrt(w ** 2 + h ** 2)

def cal_w(h: float=0, l: float=0):
    return sqrt(h ** 2 - l ** 2)

def cal_h(w: float=0, l: float=0):
    return sqrt(w ** 2 - l ** 2)
