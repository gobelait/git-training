import unittest
from sandwich_maker import Sandwich, Lettuce, SliceOfBread, Ham, Cheese


class SandwichMakerTestCase(unittest.TestCase):
    def test_create_empty_sandwich(self):
        sandwich = Sandwich()
        self.assertEqual(sandwich.size(), 0)

    def test_add_aliment_to_sandwich(self):
        sandwich = Sandwich()
        sandwich.add(Lettuce())
        self.assertEqual(sandwich.size(), 1)


if __name__ == "__main__":
    unittest.main()
