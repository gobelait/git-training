import unittest
from sandwich_maker import SandwichMaker, Lettuce, SliceOfBread, Ham, Cheese


class SandwichMakerTestCase(unittest.TestCase):
    def test_create_empty_sandwich(self):
        sandwich = SandwichMaker()
        self.assertEqual(sandwich.size(), 0)

    def test_add_aliment_to_sandwich(self):
        sandwich = SandwichMaker()
        sandwich.add(Lettuce())
        self.assertEqual(sandwich.size(), 1)


if __name__ == "__main__":
    unittest.main()
