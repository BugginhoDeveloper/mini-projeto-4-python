import unittest

from main.model import *

class TestMoneyMethods(unittest.TestCase):

    def test_separate(self):
        rights = ((2,   {2: 1}),
                       (99,  {50: 1, 20: 2, 5:1, 2: 2}),
                       (120, {100: 1, 20: 1}) )
        wrongs = ((0, 1, 3.14, -10))

        for value, result in rights:
            self.assertEqual(Money(value).separate(5), result)
        with self.assertRaises(AssertionError):
            for value in wrongs:
                Money(value).separate(5)

    def test_greater_bknote(self):
        greatidx = [(-10, -1), (1, -1), (2, 0), (3.14, 0), (4, 0), (5, 1), (20, 3), (99, 4), (100, 5), (1000, 5)]

        for value, idx in greatidx:
            self.assertEqual(Money(value).greaterBanknote(), idx)

    def test_add(self):
        testvalues = [("3.14", "2.86", "6.00"), ("20.002", "120", "140.00"), ("0.004", "0.001", "0.00")]

        for op1, op2, result in testvalues:
            self.assertEqual(Money(op1) + Money(op2), Money(result))
            self.assertEqual(Money(op1) + op2, Money(result))
            self.assertEqual(op1 + Money(op2), Money(result))

    def test_mul(self):
        test_values = [("10.01", "1.10", "11.01"), (2, 5, 10), ("500.002", "1.25", "625.0")]
        for op1, op2, result in test_values:
            self.assertEqual(Money(op1) * Money(op2), Money(result), "teste")
            self.assertEqual(Money(op1) * op2, Money(result))
            self.assertEqual(op1 * Money(op2), Money(result))

class TestAccountMethods(unittest.TestCase):
    pass

class TestUserMethods(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()