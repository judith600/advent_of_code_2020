from ErisType import EErisType
from ErisType import State


class EmptyState(State):

    def __init__(self):
        super().__init__()
        self.displaySign = '.'
        self.erisType = EErisType.EMPTY
        self.isSwitch = False

    def calculateIfSwitch(self, neighbors):
        countNeighborBugs = 0
        for elem in neighbors:
            if elem.erisType == EErisType.BUG:
                countNeighborBugs += 1
        if 0 < countNeighborBugs < 3:
            self.isSwitch = True
        return self.isSwitch

    def getIsSwitch(self):
        return self.isSwitch

    def getDisplaySign(self):
        return self.displaySign