# 15. Write a Python program to get the volume of a sphere with radius 6.

from math import pi


def volume_of_sphere(radius):
    """ (int) -> float

    Fill in the radius of a sphere and this program will calculate its volume

    volume_of_sphere(6)
    904.7786842338603
    volume_of_sphere(10)
    4188.790204786391
    """

    return 4.0/3.0 * pi * radius ** 3


print(volume_of_sphere(10))
