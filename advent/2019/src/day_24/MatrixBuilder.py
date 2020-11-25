import sys
sys.path.append('/workspace/advent_of_code_2020/advent/2019/src')
from file_opener import FileOpener
from ErisType import *
from BugState import BugState
from EmptyState import EmptyState

class MatrixBuilder():

    def __init__(self):
        self.matrix = [[EmptyState() for x in range (5)] for k in range(5)]
        self.fileOpener = FileOpener()

    def fillInitialMatrix(self):
        file = self.fileOpener.openInputFile(2019, 'input24.txt')
        input = file.read().replace('\n','')
        inputIter = iter(input)
        for line in range(len(self.matrix)):
            for elem in range(len(self.matrix[line])):
                inputSign = next(inputIter)
                if inputSign == '#':
                    self.matrix[line][elem] = BugState()
                else:
                    self.matrix[line][elem] = EmptyState()

    def printMatrix(self):
        for line in self.matrix:
            for elem in line:
                print(elem.getDisplaySign(), end='')
            print()
    
    def buildNextMatrix(self):
        neighborList = []
        for x in range(0, 4):
            neighborList.append(BugState())
        
        for line in range(len(self.matrix)):
            for elem in range(len(self.matrix[line])):
                currentState = self.matrix[line][elem]
                isSwitch = currentState.calculateIfSwitch(neighborList)
                if isSwitch:
                    self.updateCell(line, elem, currentState)
    
    def updateCell(line, elem, currentState):
        if currentState.getType() is EErisType.BUG:
            self.matrix[line][elem] = EmptyState()
        else:
            self.matrix[line][elem] = BugState()


if __name__ == "__main__":
    builder = MatrixBuilder()
    builder.fillInitialMatrix()
    builder.printMatrix()
    print('Building next matrix')
    builder.buildNextMatrix()
    builder.printMatrix()