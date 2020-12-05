import unittest

from day_5 import calculateSeatColumn


class BoardingPassTest(unittest.TestCase):

    def testCalculateSeatRow(self):
        pass

    def testCalculateSeatColumn(self):
        self.assertEqual(calculateSeatColumn("RRR"), 7)


if __name__ == "__main__":
    unittest.main();
