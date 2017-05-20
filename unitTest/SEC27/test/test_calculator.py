"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/4/29

import unittest
from SEC27.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.c = Calculator(5, 3)

    def test_add(self):
        # c = Calculator(5, 3)
        self.assertEqual(8, self.c.add())

    def test_subtract(self):
        # c= Calculator(8,4)
        self.assertEqual(4, self.c.subtract())

    def tearDown(self):
        print("delete")
        del self.c


if __name__ == '__main__':
    unittest.main()
