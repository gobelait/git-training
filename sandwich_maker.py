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


class Sandwich:
    def __init__(self):
        self.__stack = []

    def add(self, aliment):
        self.__stack.append(aliment)

    def size(self):
        return len(self.__stack)

    def __str__(self):
        composition = ""

        for aliment in self.__stack:
            composition += "\n" + aliment.name + "\n----------"

        return composition


if __name__ == "__main__":

    mySandwich = Sandwich()
    print (mySandwich.size())
    mySandwich.add(1)
    print (mySandwich.size())
