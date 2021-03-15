import unittest
from calculator import add

class CalculatorTestCase(unittest.TestCase):

    def test_add(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
