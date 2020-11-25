from enum import Enum

class EErisType(Enum):
    BUG = 'Bug',
    EMPTY = 'Empty'

class State:
    def __init__(self):
        self.displaySign: str = ''
        self.erisType: EErisType
        self.isSwitch: bool = False

    def update(self):
        if self.isSwitch:
            self.switchState()

    def switchState(self):
        raise NotImplementedError

    def calculateIfSwitch(self, neighbors: list) -> bool:
        raise NotImplementedError