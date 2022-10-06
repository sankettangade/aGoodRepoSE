import unittest
import sys
sys.path.insert(1, "../code")
import main
class TestCalculator(unittest.TestCase):

  def test_sum(self):
      self.assertEqual(main.Operations.calculator(1, 5, 6), 11, "Should be 11")
      self.assertEqual(main.Operations.calculator(1, -1, 1), 0, "Should be 0")
      self.assertEqual(main.Operations.calculator(1, 3, -4), -1, "Should be -1")

  def test_subtraction(self):
      self.assertEqual(main.Operations.calculator(2, 5, 6), -1, "Should be -1")
      self.assertEqual(main.Operations.calculator(2, -1, 1), -2, "Should be -2")
      self.assertEqual(main.Operations.calculator(2, 3, -4), 7, "Should be 7")

  def test_multiplication(self):
      self.assertEqual(main.Operations.calculator(3, 5, 6), 30, "Should be 30")
      self.assertEqual(main.Operations.calculator(3, -1, 1), -1, "Should be -1")
      self.assertEqual(main.Operations.calculator(3, -3, -4), 12, "Should be 12")

  def test_division(self):
      self.assertEqual(main.Operations.calculator(4, 36, 6), 6, "Should be 6")
      self.assertEqual(main.Operations.calculator(4, -1, 1), -1, "Should be -1")
      self.assertEqual(main.Operations.calculator(4, -12, -24), 0.5, "Should be 0.5")

if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)
