import unittest
import mathOperations

class testMathOperations(unittest.TestCase):
  def test_add(self):
        self.assertEqual(math_operations.add(2, 3), 5)
        self.assertEqual(math_operations.add(-1, 1), 0)
        self.assertEqual(math_operations.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(math_operations.subtract(10, 5), 5)
        self.assertEqual(math_operations.subtract(-1, 1), -2)
        self.assertEqual(math_operations.subtract(0, 0), 0)

    def test_divide(self):
        self.assertEqual(math_operations.divide(10, 2), 5)
        self.assertEqual(math_operations.divide(5, 2), 2.5)
        
        # Test that dividing by zero raises the correct error
        with self.assertRaises(ValueError):
            math_operations.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
