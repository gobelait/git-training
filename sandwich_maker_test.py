import unittest
from sandwich_maker import SandwichMaker, Lettuce, SliceOfBread, Ham, Cheese, Mayonnaise


class SandwichMakerTestCase(unittest.TestCase):
    def test_is_not_vegan_with_meat(self):
        sandwich = SandwichMaker()
        sandwich.add(Ham())
        self.assertFalse(sandwich.is_vegan())
    
    def test_is_not_vegan_with_dairy(self):
        sandwich = SandwichMaker()
        sandwich.add(Cheese())
        self.assertFalse(sandwich.is_vegan())
    
    def test_is_vegan(self):
        sandwich = SandwichMaker()
        sandwich.add(Lettuce())
        sandwich.add((SliceOfBread()))
        self.assertTrue(sandwich.is_vegan())

    def test_create_empty_sandwich(self):
        sandwich = SandwichMaker()
        self.assertEqual(sandwich.size(), 0)

    def test_add_aliment_to_sandwich(self):
        sandwich = SandwichMaker()
        sandwich.add(Lettuce())
        self.assertEqual(sandwich.size(), 1)

    def test_is_well_composed(self):
        sandwich = SandwichMaker()
        sandwich.add(SliceOfBread())
        sandwich.add(Lettuce())
        sandwich.add(SliceOfBread())
        self.assertTrue(sandwich.is_well_composed())
        
    def test_is_not_well_composed_no_bottom_bread(self):
        sandwich = SandwichMaker()
        sandwich.add(SliceOfBread())
        sandwich.add(Lettuce())
        self.assertFalse(sandwich.is_well_composed())
    
    def test_is_not_well_composed_no_top_bread(self):
        sandwich = SandwichMaker()
        sandwich.add(Lettuce())
        sandwich.add(SliceOfBread())
        self.assertFalse(sandwich.is_well_composed())

    def test_is_not_well_composed_no_filling(self):
        sandwich = SandwichMaker()
        sandwich.add(SliceOfBread())
        sandwich.add(SliceOfBread())
        sandwich.add(SliceOfBread())
        self.assertFalse(sandwich.is_well_composed())

    def test_get_composition(self):
        sandwich = SandwichMaker()
        sandwich.add(Lettuce())
        sandwich.add(SliceOfBread())
        composition = sandwich.get_composition()
        self.assertEqual(composition[0].name, Lettuce().name)
        self.assertEqual(composition[1].name, SliceOfBread().name)
        self.assertEqual(sandwich.size(), 2)

    def test_reset(self):
        sandwich = SandwichMaker()
        sandwich.add(Lettuce())		
        sandwich.reset()
        self.assertEqual(sandwich.size(), 0)

    def test_get_aliment_counter(self):
        expected = {"Slice of bread": 2, "Cheese": 1, "Ham": 1}
        sandwich = SandwichMaker()
        sandwich.add(SliceOfBread())
        sandwich.add(Cheese())
        sandwich.add(Ham())
        sandwich.add(SliceOfBread())
        self.assertEqual(expected, sandwich.get_aliment_counter())
    def test_is_complete(self):
        sandwich = SandwichMaker()
        sandwich.add(SliceOfBread())
        sandwich.add(Lettuce())
        sandwich.add(Mayonnaise())
        sandwich.add(SliceOfBread())
        self.assertTrue(sandwich.is_complete())

    def test_is_not_complete_with_not_well_composed(self):
        sandwich = SandwichMaker()
        sandwich.add(SliceOfBread())
        sandwich.add(Lettuce())
        sandwich.add(Mayonnaise())
        self.assertFalse(sandwich.is_complete())

    def test_is_not_complete_with_no_vegetable(self):
        sandwich = SandwichMaker()
        sandwich.add(SliceOfBread())
        sandwich.add(Mayonnaise())
        sandwich.add(SliceOfBread())
        self.assertFalse(sandwich.is_complete())

    def test_is_not_complete_with_no_sauce(self):
        sandwich = SandwichMaker()
        sandwich.add(SliceOfBread())
        sandwich.add(Lettuce())
        sandwich.add(SliceOfBread())
        self.assertFalse(sandwich.is_complete())


if __name__ == "__main__":
    unittest.main()
