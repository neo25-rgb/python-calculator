import unittest
import os
from utils import History

from utils import Calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc0 = Calculator(0)   # rounds to 0 decimal places
        self.calc2 = Calculator(2)   # rounds to 2 decimal places

    # --- Addition Tests ---
    def test_addition(self):
        self.assertEqual(self.calc0.addtion(2, 3), 5)
        self.assertEqual(self.calc2.addtion(2.111, 3.222), 5.33)
        self.assertEqual(self.calc2.addtion(-2, 5), 3.00)
        self.assertEqual(self.calc2.addtion(-2.55, -3.45), -6.00)
        self.assertEqual(self.calc2.addtion(0, 0), 0.00)
        self.assertEqual(self.calc2.addtion(123.456, 0.004), 123.46)

    # --- Subtraction Tests ---
    def test_subtraction(self):
        self.assertEqual(self.calc0.subtraction(5, 3), 2)
        self.assertEqual(self.calc2.subtraction(5.555, 2.222), 3.33)
        self.assertEqual(self.calc2.subtraction(-5, -2), -3.00)
        self.assertEqual(self.calc2.subtraction(0, 5), -5.00)
        self.assertEqual(self.calc2.subtraction(3.1459, 3.1415), 0.00)
        self.assertEqual(self.calc2.subtraction(1000.55, 0.55), 1000.00)

    # --- Multiplication Tests ---
    def test_multiplication(self):
        self.assertEqual(self.calc0.multiplication(2, 3), 6)
        self.assertEqual(self.calc2.multiplication(2.345, 3.456), 8.10)
        self.assertEqual(self.calc2.multiplication(-2, 3), -6.00)
        self.assertEqual(self.calc2.multiplication(0, 99), 0.00)
        self.assertEqual(self.calc2.multiplication(1.111, 1.111), 1.23)
        self.assertEqual(self.calc2.multiplication(12.5, 0.4), 5.00)

    # --- Division Tests ---
    def test_division(self):
        self.assertEqual(self.calc0.division(9, 3), 3)
        self.assertEqual(self.calc2.division(10, 3), 3.33)
        self.assertEqual(self.calc2.division(-10, 4), -2.50)
        self.assertEqual(self.calc2.division(5, 2), 2.50)
        self.assertEqual(self.calc2.division(7.5, 2.5), 3.00)
        self.assertEqual(self.calc2.division(0, 3), 0.00)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc0.division(5, 0)

    # --- Property Tests ---
    def test_rounding_property(self):
        self.assertEqual(self.calc2.round_digits, 2)
        self.assertEqual(self.calc0.round_digits, 0)
        self.assertIsInstance(self.calc2.round_digits, int)
        self.assertGreaterEqual(self.calc2.round_digits, 0)


        
        
        
        
class TestHistory(unittest.TestCase):
    
    def setUp(self):
        self.test_file = "test_history.txt"
        # Ensure the file is clean before each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.history = History(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_restore(self):
        self.history.save("2 + 2 = 4")
        self.history.save("3 * 3 = 9")

        lines = self.history.restore()
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0].strip(), "2 + 2 = 4")
        self.assertEqual(lines[1].strip(), "3 * 3 = 9")

    def test_clear(self):
        self.history.save("something")
        self.history.clear()

        lines = self.history.restore()
        self.assertEqual(lines, [])

    def test_restore_empty_file(self):
        # Should return an empty list if file is empty
        open(self.test_file, "w").close()
        lines = self.history.restore()
        self.assertEqual(lines, [])