import unittest

from main.model import *


class TestMoneyMethods(unittest.TestCase):
    def setUp(self):
        self.rights = ((2,   {2: 1}),
                       (99,  {50: 1, 20: 2, 5:1, 2: 2}),
                       (120, {100: 1, 20: 1}) )
        self.wrongs = ((0, 1, 3.14, -10))

    def test_separate(self):
        for value, result in self.rights:
            self.assertEqual(Money(value).separate(5), result)
        with self.assertRaises(AssertionError):
            for value in self.wrongs:
                Money(value).separate(5)


if __name__ == '__main__':
    unittest.main()