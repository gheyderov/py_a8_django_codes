import unittest
from main import sumx, divide


class Calc(unittest.TestCase):

    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b

    def test_sumx(self):
        a = 4
        b = 2
        expected_result = 6
        actual_result = sumx(a, b)
        self.assertEqual(actual_result, expected_result)

    def test_divide(self):
        a = 4
        b = 2
        expected_result = 2
        actual_result = divide(a, b)
        self.assertEqual(expected_result, actual_result)

    def test_divide_with_zero_args(self):
        a = 4
        b = 0
        self.assertRaises(ZeroDivisionError, divide, a, b)


if __name__ == '__main__':
    unittest.main()