from file_opener import getInputFileLinesAsList


def calculateSeatColumn(columnInput: str) -> int:
    if columnInput.__len__() != 3:
        raise ValueError("Input must be 7 chars long.")
    columnRange = range(8)
    return calculateNumberByDirection(columnRange, columnInput, getNextColumnRange)


def calculateSeatRow(rowInput: str) -> int:
    if rowInput.__len__() != 7:
        raise ValueError("Input must be 7 chars long.")
    rowRange = range(128)
    return calculateNumberByDirection(rowRange, rowInput, getNextRowRange)


def calculateNumberByDirection(valueRange: range, directions: str, func):
    currentRange = valueRange
    for direction in directions:
        nextRange = func(currentRange, direction)
        currentRange = nextRange
    if currentRange.__len__() == 1:
        return int(currentRange.start)


def getNextColumnRange(oldRange: range, direction: str):
    if direction == "L":
        return oldRange[0:middleOf(oldRange)]
    elif direction == "R":
        return oldRange[middleOf(oldRange):]


def getNextRowRange(oldRange: range, direction: str) -> range:
    if direction == "F":
        return oldRange[0:middleOf(oldRange)]
    elif direction == "B":
        return oldRange[middleOf(oldRange):]


def middleOf(myRange: range):
    return int(myRange.__len__() / 2)


def getIdList(file):
    idList = []
    for boardingPass in boardingPassInput:
        row = calculateSeatRow(boardingPass[0:7])
        column = calculateSeatColumn(boardingPass[7:10])
        boardingPassId = row * 8 + column
        idList.append(boardingPassId)
    return idList


def findMissingId(idList):
    lowestNumber = min(idList)
    highestNumber = max(idList)
    return [x for x in range(lowestNumber, highestNumber+1) if x not in idList]


if __name__ == "__main__":
    boardingPassInput = getInputFileLinesAsList("input_5.txt")
    idList = getIdList(boardingPassInput)
    print(idList)
    print("Highest ID: ", max(idList))
    print(idList)
    print(findMissingId(idList))
