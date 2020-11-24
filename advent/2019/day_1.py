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
    
    def calcExtraFuel(self, mass: int):
        result = 0
        massLeft = mass
        while massLeft >= 9:
            massLeft = self.calcFuelForMass(massLeft)
            result += massLeft
        return result

class FuelRequirementsTest(unittest.TestCase):
    def setUp(self):
        self.fuelRequirements = FuelRequirements()

    def test_14(self):
        self.assertEquals(2, self.fuelRequirements.calcFuelForMass(14))

    def test_1969(self):
        self.assertEqual(654, self.fuelRequirements.calcFuelForMass(1969))

    def test_100756(self):
        self.assertEqual(33583, self.fuelRequirements.calcFuelForMass(100756))

    def test_rec_100756(self):
        self.assertEqual(50346, self.fuelRequirements.calcExtraFuel(100756))

    def test_rec_9(self):
        self.assertEqual(1, self.fuelRequirements.calcExtraFuel(9))


if __name__ == "__main__":
    # unittest.main()

    fuel = FuelRequirements()
    result: int = 0
    inputListConverted = fuel.readFileInput(fuel.openInputFile())
    for elem in inputListConverted:
        result = result + fuel.calcExtraFuel(elem)
    
    print(result)