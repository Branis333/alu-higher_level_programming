#!/usr/bin/python3
"""Adds two numbers"""

<<<<<<< HEAD

def add_integer(a, b=98):
    """
    Returns sum of a and b
    - Args :
        a: int or float
        b: int or float, default 98
=======
def ass_integer(a, b=98):
    """
    Return sum of a and  b 
    - Args :
    a: int or float
    b: int or float, default 98
>>>>>>> ff4bd0fadd1b88d2ba7469651e7cfd06cd3a0813
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b
