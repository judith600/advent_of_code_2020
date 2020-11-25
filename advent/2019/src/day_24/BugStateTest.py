import unittest
from BugState import *

class BugStateTest(unittest.TestCase):

    def setUp(self):
        self.bugState = BugState()
        self.neighborList = []
        for x in range(0, 4):
            self.neighborList.append(BugState())

    def testSwitchWhenFourBugNeighbors(self):
        self.assertEqual(True, self.bugState.calculateIfSwitch(self.neighborList))

        

if __name__ == "__main__":
    unittest.main()