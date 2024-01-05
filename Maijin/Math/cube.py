"""
3D cube calculation module
"""

def volume(h: float=0, w: float=0, l: float=0):
    """
    Calculate the volume of a cube
    @param h: Height
    @param w: Width
    @param l: Length
    @return: Volume
    >>> cube.volume(1, 2, 3)
    6
    """
    return h * w * l

def surface(h: float=0, w: float=0, l: float=0):
    """
    Calculate the surface of a cube
    @param h: Height
    @param w: Width
    @param l: Length
    @return: Surface
    >>> cube.surface(1, 2, 3)
    22
    """
    return 2 * (h * w + h * l + w * l)

def diagonal(h: float=0, w: float=0, l: float=0):
    """
    Calculate the diagonal of a cube
    @param h: Height
    @param w: Width
    @param l: Length
    @return: Diagonal
    >>> cube.diagonal(1, 2, 3)
    3.7416573867739413
    """
    return (h ** 2 + w ** 2 + l ** 2) ** 0.5

def angle(h: float=0, w: float=0, l: float=0):
    """
    Calculate the angle of a cube
    @param h: Height
    @param w: Width
    @param l: Length
    @return: Angle
    >>> cube.angle(1, 2, 3)
    1.5707963267948966
    """
    return ((w **2 + l ** 2) ** 0.5) + (h ** 2) ** 0.5