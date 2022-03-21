from enum import Enum


class Nature(Enum):
    BREAD = "bread"
    MEAT = "meat"
    DAIRY = "dairy"
    VEGETABLE = "vegetable"


class Aliment:
    def __init__(self, nature, name):
        self.nature = nature
        self.name = name


class Cheese(Aliment):
    def __init__(self):
        super().__init__(Nature.DAIRY, 'Cheese')


class SliceOfBread(Aliment):
    def __init__(self):
        super().__init__(Nature.BREAD, "Slice of bread")


class Ham(Aliment):
    def __init__(self):
        super().__init__(Nature.MEAT, "Ham")


class Lettuce(Aliment):
    def __init__(self):
        super().__init__(Nature.VEGETABLE, "Lettuce")


class SandwichMaker:
    def __init__(self):
        self.__sandwich = []

    def add(self, aliment):
        self.__sandwich.append(aliment)

    def size(self):
        return len(self.__sandwich)

    def is_well_composed(self):
        is_top_bread = self.__sandwich[0].nature == Nature.BREAD
        is_bottom_bread = self.__sandwich[-1].nature == Nature.BREAD
        has_filling = False

        for item in self.__sandwich:
            if item.nature != Nature.BREAD:
                has_filling = True
        
        return (
             is_top_bread and is_bottom_bread and has_filling
        )


    def get_composition(self):
        return self.__sandwich


    def __str__(self):
        composition = ""

        for aliment in self.__sandwich:
            composition += "\n" + aliment.name + "\n----------"

        return composition