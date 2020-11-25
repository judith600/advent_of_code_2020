import unittest as unittest
import math as m
import os
from file_opener import *

class FuelRequirements():

    def calcFuelForMass(self, mass: int):
        return m.floor(mass / 3) - 2
    
    def calcExtraFuel(self, mass: int):
        result = 0
        massLeft = mass
        while massLeft >= 9:
            massLeft = self.calcFuelForMass(massLeft)
            result += massLeft
        return result

if __name__ == "__main__":
    fuel = FuelRequirements()
    fileOpener = FileOpener()
    result: int = 0
    inputListConverted = fileOpener.readFileInput(fileOpener.openInputFile(2019, 'input.txt'))
    for elem in inputListConverted:
        result = result + fuel.calcExtraFuel(elem)
    
    print(result)