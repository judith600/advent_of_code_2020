import copy

from advent.year2019.src.day_24.BugState import BugState
from advent.year2019.src.day_24.EmptyState import EmptyState


class MatrixBuilder:

    def __init__(self):
        self.matrix = [[EmptyState() for x in range(5)] for k in range(5)]
        self.MIN = 0
        self.MAX = 4

    def fillInitialMatrix(self):
        file = open('input24.txt')
        fileInput = file.read().replace('\n', '')
        inputIter = iter(fileInput)
        for line in range(len(self.matrix)):
            for elem in range(len(self.matrix[line])):
                inputSign = next(inputIter)
                if inputSign == '#':
                    self.matrix[line][elem] = BugState()
                else:
                    self.matrix[line][elem] = EmptyState()

    def printMatrix(self, matrix):
        for line in matrix:
            for elem in line:
                print(elem.getDisplaySign(), end='')
            print()

    def setMatrix(self, matrix):
        self.matrix = copy.deepcopy(matrix)

    def buildNextMatrix(self):
        copyMatrix = copy.deepcopy(self.matrix)
        for line in range(len(self.matrix)):
            for elem in range(len(self.matrix[line])):
                neighborList = self.getNeighbors(self.matrix, line, elem)
                currentState = self.matrix[line][elem]
                isSwitch = currentState.calculateIfSwitch(neighborList)
                if isSwitch:
                    self.updateCell(line, elem, currentState, copyMatrix)
        return copyMatrix

    def updateCell(self, line, elem, currentState, copyMatrix):
        if type(currentState) is BugState:
            copyMatrix[line][elem] = EmptyState()
        else:
            copyMatrix[line][elem] = BugState()

    def getNeighbors(self, matrix, line, elem):
        neighborList = [self.getLeftNeighbor(matrix, line, elem), self.getUpperNeighbor(matrix, line, elem),
                        self.getRightNeighbor(matrix, line, elem), self.getLowerNeighbor(matrix, line, elem)]
        return neighborList

    def getLeftNeighbor(self, matrix, line, elem):
        if elem > self.MIN:
            return matrix[line][elem - 1]
        else:
            return EmptyState()

    def getUpperNeighbor(self, matrix, line, elem):
        if line > self.MIN:
            return matrix[line - 1][elem]
        else:
            return EmptyState()

    def getRightNeighbor(self, matrix, line, elem):
        if elem < self.MAX:
            return matrix[line][elem + 1]
        else:
            return EmptyState()

    def getLowerNeighbor(self, matrix, line, elem):
        if line < self.MAX:
            return matrix[line + 1][elem]
        else:
            return EmptyState()


class MatrixCollectorAndComparator:
    def __init__(self, builder: MatrixBuilder):
        self.allMatrices = []
        self.builder = builder

    def addMatrix(self, matrix):
        self.allMatrices.append(matrix)

    def iterateUntilDuplicate(self):
        self.builder.fillInitialMatrix()
        self.builder.printMatrix(builder.matrix)

        while True:
            print('Calculating next matrix!!!')
            nextMatrix = builder.buildNextMatrix()
            builder.setMatrix(nextMatrix)
            self.builder.printMatrix(builder.matrix)

            matrixString = self.buildStringFromMatrix(builder.matrix)
            # compare
            for matrix in self.allMatrices:
                if matrix == matrixString:
                    print('found duplicate matrix !!!')
                    return matrixString

            self.allMatrices.append(matrixString)

    def buildStringFromMatrix(self, matrix):
        matrixString = ''
        for line in matrix:
            for elem in line:
                matrixString += elem.displaySign
        return matrixString

    def calculateBiodiversity(self, matrix):
        biodiversity = 0
        for index, char in enumerate(matrix):
            if char == '#':
                biodiversity += pow(2, index)
        return biodiversity


if __name__ == "__main__":
    builder = MatrixBuilder()
    collector = MatrixCollectorAndComparator(builder)
    duplicateMatrix = collector.iterateUntilDuplicate()
    print(collector.calculateBiodiversity(duplicateMatrix))
