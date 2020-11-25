from ErisType import State
from ErisType import EErisType
import BugState

class EmptyState(State):

    def __init__(self):
        super().__init__()
        self.displaySign = '.'
        self.erisType = EErisType.EMPTY

    def calculateIfSwitch(self, neighbors):
        return super().calculateIfSwitch(neighbors)
        countNeighborBugs = 0
        for elem in neighbors:
            if type(elem) == State and elem.erisType == EErisType.BUG:
                countNeighborBugs += 1
        if 0 < countNeighborBugs < 3:
            self.isSwitch = True
        return self.isSwitch

    def switchState(self):
        return BugState()

    def getIsSwitch(self):
        return self.isSwitch