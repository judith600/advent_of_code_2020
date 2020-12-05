from file_opener import getInputFileLinesAsList


def calculateSeatColumn(columnInput: str) -> int:
    columnRange = range(8)
    return calculateNumberByDirection(columnRange, columnInput, getNextColumnRange)


def calculateSeatRow(rowInput: str) -> int:
    rowRange = range(128)
    return calculateNumberByDirection(rowRange, rowInput, getNextRowRange)


def calculateNumberByDirection(valueRange: range, directions: str, func):
    currentRange = valueRange
    for direction in directions:
        nextRange = func(currentRange, direction)
        currentRange = nextRange
    if currentRange.start is currentRange.stop:
        return int(currentRange.start)


def getNextColumnRange(oldRange: range, direction: str):
    if direction == "L":
        return oldRange[0:middleOf(oldRange) - 1]
    elif direction == "R":
        return oldRange[middleOf(oldRange):]


def getNextRowRange(oldRange: range, direction: str) -> range:
    if direction == "F":
        return oldRange[0:middleOf(oldRange) - 1]
    elif direction == "B":
        return oldRange[middleOf(oldRange):]


def middleOf(myRange: range):
    return int(myRange.__len__() / 2)


def getIdList(file):
    idList = []
    for boardingPass in boardingPassInput:
        row = calculateSeatRow(boardingPass[0:6])
        column = calculateSeatColumn(boardingPass[7:9])
        boardingPassId = row * 8 + column
        idList.append(boardingPassId)
    return idList


if __name__ == "__main__":
    boardingPassInput = getInputFileLinesAsList("input_5.txt")
    idList = getIdList(boardingPassInput)
    print(idList)
    print("Highest ID: ", max(idList))
