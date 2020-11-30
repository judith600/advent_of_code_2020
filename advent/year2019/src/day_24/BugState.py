from ErisType import EErisType
from ErisType import State


class BugState(State):
    
    def __init__(self):
        super().__init__()
        self.displaySign = '#'
        self.erisType = EErisType.BUG
        self.isSwitch = False

    def calculateIfSwitch(self, neighbors) -> bool:
        self.isSwitch = False
        countNeighborBugs = 0
        for elem in neighbors:
            if elem.erisType == EErisType.BUG:
                countNeighborBugs += 1
        if countNeighborBugs != 1:
            self.isSwitch = True
        return self.isSwitch

    def getIsSwitch(self):
        return self.isSwitch

    def getDisplaySign(self):
        return self.displaySign
        

if __name__ == "__main__":
    print('start')
    bug = BugState()