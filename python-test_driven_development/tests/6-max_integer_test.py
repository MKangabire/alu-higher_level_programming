#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([2, 7, 1, 10]), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, -10]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 0, 10, -3, 8]), 10)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([3.5, 1.2, 4.8]), 4.8)
    
    def test_max_at_beginning(self):
        self.assertEqual(max_integer([3.5, 1.2, 2.8], 3.5)

if __name__ == '__main__':
    unittest.main()
