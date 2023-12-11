#!/usr/bin/python3
<<<<<<< HEAD
"""Doc"""
=======
""""Doc"""

>>>>>>> 2bbca3d47bdf7221149f28bea47d7356b032b0a6

import unittest

max_integer = __import__('6-max_integer').max_integer

<<<<<<< HEAD
class TestMaxInteger(unittest.TestCase):
    """Doc"""

    def test_simple_case(self):
        """Doc"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative_case(self):
        """Doc"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_empty_case(self):
        """Doc"""
        self.assertEqual(max_integer([]), None)

    def test_max_middle_case(self):
        """Doc"""
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_one_element_case(self):
        """Doc"""
        self.assertEqual(max_integer([5]), 5)

=======

class TestMaxInteger(unittest.TestCase):
    """"Doc"""

    def test_simple_case(self):
        """"Doc"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative_case(self):
        """"Doc"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_empty_case(self):
        """"Doc"""
        self.assertEqual(max_integer([]), None)

    def test_max_middle_case(self):
        """"Doc"""
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_one_element_case(self):
        """"Doc"""
        self.assertEqual(max_integer([5]), 5)
>>>>>>> 2bbca3d47bdf7221149f28bea47d7356b032b0a6
