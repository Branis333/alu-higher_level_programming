#!/usr/bin/python3
"""Doc"""
<<<<<<< HEAD
 

def say_my_name(first_name, last_name=""):
    """Doc"""
=======


def say_my_name(first_name, last_name=""):
    """"Doc"""
>>>>>>> 2bbca3d47bdf7221149f28bea47d7356b032b0a6
    if not isinstance(first_name, (str,)):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, (str,)):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
