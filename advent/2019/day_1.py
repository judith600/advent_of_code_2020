import unittest as unittest
import math as m
import os

class FuelRequirements():

    def calcFuelForMass(self, mass: int):
        return m.floor(mass / 3) - 2

    def openInputFile(self):
        return open('./advent/2019/resources/input.txt')
    
    def readFileInput(self, file) -> list:
        inputList: list[str] = file.readlines()
        inputListConverted: list = []
        for elem in inputList:
            elemNoLineBreak: str = elem.replace("\n", "")
            if elemNoLineBreak.isdigit():
                inputListConverted.append(int(elemNoLineBreak))
        return inputListConverted


class FuelRequirementsTest(unittest.TestCase):
    def setUp(self):
        self.fuelRequirements = FuelRequirements()

    def test_14(self):
        self.assertEquals(2, self.fuelRequirements.calcFuelForMass(14))

    def test_1969(self):
        self.assertEquals(654, self.fuelRequirements.calcFuelForMass(1969))

    def test_100756(self):
        self.assertEquals(33583, self.fuelRequirements.calcFuelForMass(100756))


if __name__ == "__main__":
    # unittest.main()

    fuel = FuelRequirements()
    result = 0
    inputListConverted = fuel.readFileInput(fuel.openInputFile())
    for elem in inputListConverted:
        result = result + fuel.calcFuelForMass(elem)

    print(result)