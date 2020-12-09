from typing import List, Tuple

from file_opener import getInputFileLinesAsList

mapTemplate = getInputFileLinesAsList("src/part_one/day_1/input")
highestIndex = len(mapTemplate[0]) - 1
lastLine = len(mapTemplate) - 1


def traverseMapAndCountTrees(indexStep: int, lineStep: int, counter=0, currentLine=0, index=0) -> int:
    if currentLine > lastLine:
        return counter
    line = mapTemplate[currentLine]
    currentSign = line[index]
    if currentSign == "#":
        counter += 1
    print("Being on line: ", currentLine, " index: ", index, " sign: ", currentSign, " counter: ", counter)
    index += indexStep
    return traverseMapAndCountTrees(indexStep, lineStep, counter, currentLine + lineStep, calculateNextIndex(index))


def calculateNextIndex(index):
    if isBumpAtRightEnd(index):
        residue = indexResidue(index)
        if residue > 0:
            nextIndex = residue - 1
        else:
            nextIndex = 0
    else:
        nextIndex = index
    return nextIndex


def isBumpAtRightEnd(index):
    difference = highestIndex - index
    return difference < 0


def indexResidue(index):
    return abs(highestIndex - index)


def traverseDifferentSlopes(stepPairs: List[Tuple]):
    trees = 1
    for pair in stepPairs:
        trees *= traverseMapAndCountTrees(indexStep=pair[0], lineStep=pair[1])
    return trees


if __name__ == '__main__':
    print(mapTemplate)
    print(traverseMapAndCountTrees(indexStep=3, lineStep=1))
    print(traverseDifferentSlopes([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
