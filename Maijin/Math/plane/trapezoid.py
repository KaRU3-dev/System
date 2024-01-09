"""
台形
"""

from cmath import sqrt, tan

def trapezoid_area(bottom, upper, height):
    """
    台形の面積を求める
    """
    return (bottom + upper) * height / 2

def trapezoid_sidereal_length(bottom, upper, left, right):
    """
    台形の周囲の長さを求める
    """
    return bottom + upper + left + right

def trapezoid_height(bottom, upper, left, right):
    """
    台形の高さを求める
    """
    return (left ** 2 - right ** 2 + bottom ** 2 - upper ** 2) / (2 * (bottom - upper))

def trapezoid_bottom(height, left, right):
    """
    台形の下底を求める
    """
    return (2 * height * (left + right) - (left ** 2 - right ** 2)) / (2 * (left + right))

def trapezoid_upper(height, left, right):
    """
    台形の上底を求める
    """
    return (2 * height * (left + right) + (left ** 2 - right ** 2)) / (2 * (left + right))

def trapezoid_left(bottom, upper, height):
    """
    台形の左斜辺を求める
    """
    return sqrt((bottom - upper) ** 2 + height ** 2)

def trapezoid_right(bottom, upper, height):
    """
    台形の右斜辺を求める
    """
    return sqrt((bottom - upper) ** 2 + height ** 2)
