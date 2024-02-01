# test_calculator.py
import unittest
from calculator_logic import safe_eval

class TestCalculatorLogic(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(safe_eval("1+1"), 2)

    def test_subtraction(self):
        self.assertEqual(safe_eval("2-1"), 1)

    def test_multiplication(self):
        self.assertEqual(safe_eval("3*3"), 9)

    def test_division(self):
        self.assertEqual(safe_eval("12/3"), 4)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            safe_eval("1/0")
        self.assertIn("Division by zero is not allowed.", str(context.exception))

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            safe_eval("invalid_expression")

    def test_empty_expression(self):
        with self.assertRaises(ValueError):
            safe_eval("")

if __name__ == '__main__':
    unittest.main()
