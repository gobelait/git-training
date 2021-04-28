from enum import Enum


class Nature(Enum):
    BREAD = "bread"
    MEAT = "meat"
    DAIRY = "dairy"
    VEGETABLE = "vegetable"
    SAUCE = "sauce"


class Aliment:
    def __init__(self, nature, name):
        self.nature = nature
        self.name = name


class Mayonnaise(Aliment):
    def __init__(self):
        super().__init__(Nature.SAUCE, 'Mayonnaise')


class Butter(Aliment):
    def __init__(self):
        super().__init__(Nature.DAIRY, 'Butter')


class Cheese(Aliment):
    def __init__(self):
        super().__init__(Nature.DAIRY, "Cheese")


class SliceOfBread(Aliment):
    def __init__(self):
        super().__init__(Nature.BREAD, "Slice of bread")


class Ham(Aliment):
    def __init__(self):
        super().__init__(Nature.MEAT, "Ham")


class Lettuce(Aliment):
    def __init__(self):
        super().__init__(Nature.VEGETABLE, "Lettuce")


class Sandwich:
    def __init__(self):
        self.__stack = []

    def is_vegan(self):
        for aliment in self.__stack:
            if aliment.nature == Nature.MEAT or aliment.nature == Nature.DAIRY:
                return False
        return True

    def add(self, aliment):
        self.__stack.append(aliment)

    def size(self):
        return len(self.__stack)

    def remove_last(self):
        self.__stack.pop()

    def is_well_composed(self):
        return (
            self.__stack[0].nature == Nature.BREAD
            and self.__stack[self.size() - 1].nature == Nature.BREAD
        )

    def reset(self):
        self.__stack = []

    def __str__(self):
        composition = ""

        for aliment in self.__stack:
            composition += "\n" + aliment.name + "\n----------"

        return composition
