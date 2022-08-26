import unittest
from Operations import calculator

class TestCalculator(unittest.TestCase):

  def test_sum(self):
      self.assertEqual(calculator(1, 5, 6), 11, "Should be 11")
      self.assertEqual(calculator(1, -1, 1), 0, "Should be 0")
      self.assertEqual(calculator(1, 3, -4), -1, "Should be -1")

  def test_subtraction(self):
      self.assertEqual(calculator(1, 5, 6), -1, "Should be -1")
      self.assertEqual(calculator(1, -1, 1), -2, "Should be -2")
      self.assertEqual(calculator(1, 3, -4), 7, "Should be 7")

  def test_multiplication(self):
      self.assertEqual(calculator(1, 5, 6), 30, "Should be 30")
      self.assertEqual(calculator(1, -1, 1), -1, "Should be -1")
      self.assertEqual(calculator(1, -3, -4), 12, "Should be 12")

  def test_division(self):
      self.assertEqual(calculator(1, 36, 6), 6, "Should be 6")
      self.assertEqual(calculator(1, -1, 1), -1, "Should be -1")
      self.assertEqual(calculator(1, -12, -24), 0.5, "Should be 0.5")

if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)
