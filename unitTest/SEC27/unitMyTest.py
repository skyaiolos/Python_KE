"""
#  Script Description:
        单元测试


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/4/29
import unittest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


class MyTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(8, add(5, 3))

    def test_subtract(self):
        self.assertEqual(2, subtract(5, 3))


if __name__ == '__main__':
    unittest.main()
