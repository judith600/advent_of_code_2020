import sys
sys.path.append('/workspace/advent_of_code_2020/advent/2019/src')
import unittest
from day_1 import FuelRequirements

class FuelRequirementsTest(unittest.TestCase):
    def setUp(self):
        self.fuelRequirements = FuelRequirements()

    def test_14(self):
        self.assertEqual(2, self.fuelRequirements.calcFuelForMass(14))

    def test_1969(self):
        self.assertEqual(654, self.fuelRequirements.calcFuelForMass(1969))

    def test_100756(self):
        self.assertEqual(33583, self.fuelRequirements.calcFuelForMass(100756))

    def test_rec_100756(self):
        self.assertEqual(50346, self.fuelRequirements.calcExtraFuel(100756))

    def test_rec_9(self):
        self.assertEqual(1, self.fuelRequirements.calcExtraFuel(9))


if __name__ == "__main__":
    unittest.main()