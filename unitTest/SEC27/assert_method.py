"""
#  Script Description:
        单元测试, 断言方法.

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/4/29
import unittest

person = {'name': 'Mike', 'age': 28}
numbers = [1, 3, 2, 88, 7, 44]
s = '优品课堂 codeclassroom.com'


class TestAssert(unittest.TestCase):
    def test_assert_method(self):
        self.assertEqual('Mike', person.get('name'))

    def test_assert_true(self):
        self.assertTrue('优品课堂' in s)

    def test_assert_in(self):
        self.assertIn('优品课堂', s)

    def test_assert_float(self):
        # self.assertEqual(3.3, 1.1 + 2.2)  # AssertionError: 3.3 != 3.3000000000000003
        self.assertAlmostEqual(3.3, 1.1 + 2.2)

    def test_assert_is(self):
        self.assertIs(True + 1, 3)

    def test_assert_isNone(self):
        self.assertIsNone(person.get('Nome', None))

    def test_assert_greater(self):
        self.assertGreater(-7, numbers[0])


if __name__ == '__main__':
    unittest.main()
