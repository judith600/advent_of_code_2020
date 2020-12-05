import unittest

from day_5 import calculateSeatColumn, calculateSeatRow


class BoardingPassTest(unittest.TestCase):

    def testCalculateSeatRow(self):
        self.assertEqual(calculateSeatRow("BFFFBBF"), 70)

    def testCalculateSeatColumn(self):
        self.assertEqual(calculateSeatColumn("RRR"), 7)

    def testGetId(self):
        col = calculateSeatColumn("RRR")
        row = calculateSeatRow("FFFBBBF")
        self.assertEqual(row * 8 + col, 119)


if __name__ == "__main__":
    unittest.main()
