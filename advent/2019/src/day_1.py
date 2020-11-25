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

if __name__ == "__main__":
    fuel = FuelRequirements()
    result: int = 0
    inputListConverted = fuel.readFileInput(fuel.openInputFile())
    for elem in inputListConverted:
        result = result + fuel.calcExtraFuel(elem)
    
    print(result)