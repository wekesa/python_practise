"""
Design a multi-location tracker on map
Focus
- Only focuses on finding and displaying multiple users across the map
- Assume that people are moving or not moving
- Location tracking be local to some set location (which can be anywhere)

Out of Scope:
 - Direction
 -
"""
import math


def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for index, value in enumerate(inputArray):
        if value == elemToReplace:
            inputArray[index] = substitutionElem
    return inputArray


"""
5 * 5 * 5 = 125 True
72 
"""


def is_power(n):
    """
    - @desc calculates the 
    :param n:
    :return:
    """
    if n == 1:
        return True
    if n < 4:
        return False
    for i in range(2, int(math.sqrt(n))):
        power = i*i
        while power <= n:
            if power == n:
                return True
            power *= i
    return False


print(is_power(8))
