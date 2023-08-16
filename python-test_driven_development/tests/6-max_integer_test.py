#!/usr/bin/python3
"""
unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
ValueToSmallError = __import__('value_to_small').ValueToSmallError


class TestMaxInteger(unittest.TestCase):
    """
    This is a class built for handing testMaxIntegerCases.

    This test cases are for my 6-max_integer.py

    This test case will have about 6 cases that

    are methods and, I will handle at first and then

    fix in my 6-max_integer.py file.
    """

    def testOtherDataTypeAsArguement(self):
        """
        This raises a TypeError

        if the arguement is not a list type

        and gives the message

        "Arguement should be of Datatype list"
        """
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, "hello")
        self.assertRaises(TypeError, max_integer, "[1, 2, 4]")
        self.assertRaises(TypeError, max_integer, "13456")
        self.assertRaises(TypeError, max_integer, 3.567)
        self.assertRaises(TypeError, max_integer, 0.34)
        self.assertRaises(TypeError, max_integer, 23456)
        self.assertRaises(TypeError, max_integer, 1000)
        self.assertRaises(TypeError, max_integer, (1, 3, 4, 6))
        self.assertRaises(TypeError, max_integer, {"list": [1, 2, 3, 4]})
        self.assertRaises(TypeError, max_integer, 2+3j)

    def testDataTypeInNonEmptyList(self):
        """
        This raise a TypeError

        if the value in a list

        is not of type int with message

        f"value {value_type} not of data type int"
        """
        self.assertRaises(TypeError, max_integer, [2, 1, 5, 6, True])
        self.assertRaises(TypeError, max_integer, ["hello", 1, 5, 6, 7])
        self.assertRaises(TypeError, max_integer, [2, 1, 3.57, 6, 7])
        self.assertRaises(TypeError, max_integer, [2, 1, 5, [1, 4, 5], 34])
        self.assertRaises(TypeError, max_integer, [{"name": "Adam"}, 6, 5])
        self.assertRaises(TypeError, max_integer, [2, 1, 5, (1,)])
        self.assertRaises(TypeError, max_integer, [2, 1, 5, 6, None])

    def testLengthOfListIntegers(self):
        """
        This helps to check if the

        length of a list of integer

        is greater than 1 and raises

        a ValueToSmallError if not.
        """
        self.assertRaises(ValueToSmallError, max_integer, [2])
        self.assertRaises(ValueToSmallError, max_integer, [-3])
        self.assertRaises(ValueToSmallError, max_integer, [20])
        self.assertRaises(ValueToSmallError, max_integer, [-40])
