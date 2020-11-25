from Type import State

class BugState(State):
    
    def __init__(self):
        super().__init__()
        self.displaySign = '#'
    
    def switchState(self):
        return ''

    def calculateIfSwitch(self, neighbors):
        return super().calculateIfSwitch(neighbors)

if __name__ == "__main__":
    print('start')
    bug = BugState()