import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(5, 6), 11)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(7, 4), 3)
        self.assertEqual(self.calc.subtract(8, 6), 2)    

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(8, 6), 48)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(18, 9), 2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(19, 3), 1)
        self.assertEqual(self.calc.modulo(27, 5), 2)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()
    