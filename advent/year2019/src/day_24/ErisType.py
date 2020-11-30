from enum import Enum


class EErisType(Enum):
    BUG = 1,
    EMPTY = 2


class State:
    def __init__(self):
        self.erisType = EErisType
        self.displaySign: str = ''
        self.isSwitch: bool = False

    def getType(self):
        return self.erisType

    def switchState(self):
        raise NotImplementedError

    def calculateIfSwitch(self, neighbors: list) -> bool:
        raise NotImplementedError
