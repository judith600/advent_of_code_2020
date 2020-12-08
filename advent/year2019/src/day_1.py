import math as m

from advent.year2019.src.file_opener import readFileInput, openInputFile


def calcFuelForMass(mass: int):
    return m.floor(mass / 3) - 2


class FuelRequirements():

    def calcExtraFuel(self, mass: int):
        result = 0
        massLeft = mass
        while massLeft >= 9:
            massLeft = calcFuelForMass(massLeft)
            result += massLeft
        return result


if __name__ == "__main__":
    fuel = FuelRequirements()
    result: int = 0
    inputListConverted = readFileInput(openInputFile(2019, 'input'))
    for elem in inputListConverted:
        result = result + fuel.calcExtraFuel(elem)

    print(result)
