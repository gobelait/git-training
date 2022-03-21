import unittest
from sandwich_maker import SandwichMaker, Lettuce, SliceOfBread, Ham, Cheese


class SandwichMakerTestCase(unittest.TestCase):
    def test_is_vegetarian(self):
        sandwich = SandwichMaker()
        sandwich.add(Lettuce())
        self.assertTrue(sandwich.is_vegetarian())
    
    def test_is_not_vegetarian(self):
        sandwich = SandwichMaker()
        sandwich.add(Ham())
        self.assertFalse(sandwich.is_vegetarian())

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


if __name__ == "__main__":
    unittest.main()
