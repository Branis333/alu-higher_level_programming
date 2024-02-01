#!/usr/bin/python3
<<<<<<< HEAD
"""Doc"""

def print_square(size):
    """Doc"""
=======
""""Doc"""


def print_square(size):
    """"Doc"""
>>>>>>> 2bbca3d47bdf7221149f28bea47d7356b032b0a6
    if not isinstance(size, (int,)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

<<<<<<< HEAD
    for  _ in range(size):
=======
    for _ in range(size):
>>>>>>> 2bbca3d47bdf7221149f28bea47d7356b032b0a6
        print("#" * size)
