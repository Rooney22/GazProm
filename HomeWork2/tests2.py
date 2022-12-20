import unittest
from Question2 import largest_number


class TestQuestion1(unittest.TestCase):
    def test1(self):
        n = 3
        numbers = '1 783 2'
        result = largest_number(n, numbers)
        expected = "78321"
        self.assertEqual(result, expected)

    def test2(self):
        n = 5
        numbers = '2 4 5 2 10'
        result = largest_number(n, numbers)
        expected = "542210"
        self.assertEqual(result, expected)

    def test3(self):
        n = 3
        numbers = '991 99 9'
        result = largest_number(n, numbers)
        expected = "999991"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()