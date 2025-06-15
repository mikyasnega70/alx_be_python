import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, -2), -3)
        self.assertEqual(self.calc.add(-1, 7), 6)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        self.assertEqual(self.calc.subtract(2, 5), -3)
        self.assertEqual(self.calc.subtract(8, 8), 0)
        self.assertEqual(self.calc.subtract(7, 0), 7)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)
        self.assertEqual(self.calc.multiply(-4, 2), -8)
        self.assertEqual(self.calc.multiply(-4, -2), 8)
        self.assertEqual(self.calc.multiply(0, 2), 0)
    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-8, 2), 4)
        self.assertEqual(self.calc.divide(-4, -4), 1)
        self.assertEqual(self.calc.divide(0, 3), 0)
    def test_divide_by_zero(self):
        self.assertEqual(self.calc.divide(6, 0))
        self.assertEqual(self.calc.divide(10, 0))


