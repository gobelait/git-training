import unittest
from sandwich_maker import Sandwich, Lettuce, SliceOfBread, Ham, Cheese, Mayonnaise, create_club_sandwich


class SandwichMakerTestCase(unittest.TestCase):
    def test_create_empty_sandwich(self):
        sandwich = Sandwich()
        self.assertEqual(sandwich.size(), 0)

    def test_is_not_vegan_with_dairy(self):
        sandwich = Sandwich()
        sandwich.add(Cheese())
        self.assertFalse(sandwich.is_vegan())

    def test_is_not_vegan_with_meat(self):
        sandwich = Sandwich()
        sandwich.add(Ham())
        sandwich.add(SliceOfBread())
        self.assertFalse(sandwich.is_vegan())

    def test_is_vegan(self):
        sandwich = Sandwich()
        sandwich.add(Lettuce())
        self.assertTrue(sandwich.is_vegan())

    def test_add_aliment_to_sandwich(self):
        sandwich = Sandwich()
        sandwich.add(Lettuce())
        self.assertEqual(sandwich.size(), 1)

    def test_is_well_composed(self):
        sandwich = Sandwich()
        sandwich.add(SliceOfBread())
        sandwich.add(Lettuce())
        sandwich.add(SliceOfBread())
        self.assertTrue(sandwich.is_well_composed())

    def test_is_not_well_composed(self):
        sandwich = Sandwich()
        sandwich.add(SliceOfBread())
        sandwich.add(Lettuce())
        self.assertFalse(sandwich.is_well_composed())

    def test_reset(self):
        sandwich = Sandwich()
        sandwich.add(Lettuce())
        sandwich.reset()
        self.assertEqual(sandwich.size(), 0)

    def test_get_composition(self):
        expected = {"Slice of bread": 2, "Cheese": 1, "Ham": 1}
        sandwich = Sandwich()
        sandwich.add(SliceOfBread())
        sandwich.add(Cheese())
        sandwich.add(Ham())
        sandwich.add(SliceOfBread())
        self.assertEqual(expected, sandwich.get_composition())

    def test_remove_last_aliment(self):
        sandwich = Sandwich()
        sandwich.add(Lettuce())
        sandwich.add(Lettuce())
        sandwich.remove_last()
        self.assertEqual(sandwich.size(), 1)

    def test_is_complete(self):
        sandwich = Sandwich()
        sandwich.add(SliceOfBread())
        sandwich.add(Lettuce())
        sandwich.add(Mayonnaise())
        sandwich.add(SliceOfBread())
        self.assertTrue(sandwich.is_complete())

    def test_is_not_complete_with_not_well_composed(self):
        sandwich = Sandwich()
        sandwich.add(SliceOfBread())
        sandwich.add(Lettuce())
        sandwich.add(Mayonnaise())
        self.assertFalse(sandwich.is_complete())

    def test_is_not_complete_with_no_vegetable(self):
        sandwich = Sandwich()
        sandwich.add(SliceOfBread())
        sandwich.add(Mayonnaise())
        sandwich.add(SliceOfBread())
        self.assertFalse(sandwich.is_complete())

    def test_is_not_complete_with_no_sauce(self):
        sandwich = Sandwich()
        sandwich.add(SliceOfBread())
        sandwich.add(Lettuce())
        sandwich.add(SliceOfBread())
        self.assertFalse(sandwich.is_complete())

    def test_create_club_sandwich_is_complete(self):
        club = create_club_sandwich()
        self.assertTrue(club.is_complete())


if __name__ == "__main__":
    unittest.main()
