from copy import deepcopy

from file_opener import *


def getSeatMap(fileName):
    myList = getInputFileLinesAsList(fileName)
    seatList = []
    for line in myList:
        seatList.append(list(line))
    return seatList


def getAdjcacentSeats(seatMap, lineI, seatI) -> int:
    neighbours = [getSeatWithIndices(seatMap, lineI, seatI - 1),
                  getSeatWithIndices(seatMap, lineI, seatI + 1),
                  getSeatWithIndices(seatMap, lineI - 1, seatI),
                  getSeatWithIndices(seatMap, lineI + 1, seatI),
                  getSeatWithIndices(seatMap, lineI - 1, seatI - 1),
                  getSeatWithIndices(seatMap, lineI - 1, seatI + 1),
                  getSeatWithIndices(seatMap, lineI + 1, seatI - 1),
                  getSeatWithIndices(seatMap, lineI + 1, seatI + 1)]
    adjacentOccupied = [s for s in neighbours if s == '#']
    return len(adjacentOccupied)


def getSeatWithIndices(seatMap, lineI, seatI):
    maxSeat = len(seatMap[0])
    maxLine = len(seatMap)
    if (seatI < 0 or seatI >= maxSeat) or (lineI < 0 or lineI >= maxLine):
        return None
    else:
        return seatMap[lineI][seatI]


def changeStateIfNeeded(copiedSeatMap, seat, lineI, seatI, adjacent, counter):
    if seat == '.':
        pass
    elif seat == 'L' and adjacent == 0:
        counter += 1
        copiedSeatMap[lineI][seatI] = '#'
    elif seat == '#' and adjacent >= 4:
        counter += 1
        copiedSeatMap[lineI][seatI] = 'L'
    return counter


def calculateNextSeatMap(seatMap):
    changedSeatsCounter = 0
    copy = deepcopy(seatMap)
    for lineIndex, line in enumerate(seatMap):
        for seatIndex, seat in enumerate(line):
            adjacent = getAdjcacentSeats(seatMap, lineIndex, seatIndex)
            changedSeatsCounter = changeStateIfNeeded(copy, seat, lineIndex, seatIndex, adjacent, changedSeatsCounter)
    return copy, changedSeatsCounter


def repeatUntilNoSeatsChange(seatList):
    myNextSeats, counter = calculateNextSeatMap(seatList)
    # for line in myNextSeats:
    # print(line)
    print('Changed seats: ', counter)
    while counter > 0:
        myNextSeats, counter = calculateNextSeatMap(myNextSeats)
        print('Changed seats: ', counter)

    occupied = 0
    for line in myNextSeats:
        occupied += line.count('#')
    print('Occupied seats: ', occupied)


if __name__ == '__main__':
    seats = getSeatMap("input")
    repeatUntilNoSeatsChange(seats)
