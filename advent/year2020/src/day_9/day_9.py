from copy import deepcopy
from typing import List

from file_opener import getInputFileLinesAsList


def parseData(fileName):
    numberStrings = getInputFileLinesAsList(fileName)
    return [int(line) for line in numberStrings]


def isCurrentNumberValid(current: int, scope: List[int]):
    for index, firstNum in enumerate(scope):
        for secondNum in scope[index + 1:]:
            if firstNum + secondNum == current:
                return True
    return False


def getCurrentScope(currentIndex):
    copy = deepcopy(numbers)
    return copy[currentIndex - 25: currentIndex]


def tryFromIndexOn(numbers, indexToStart):
    myIter = iter(numbers[indexToStart:])
    mySum = 0
    summandList = []
    while mySum < 70639851:
        follower = next(myIter)
        summandList.append(follower)
        mySum += follower
    if mySum == 70639851:
        return summandList
    else:
        return None


def findContiguousSet(numberList):
    for index, number in enumerate(numberList):
        resultList = tryFromIndexOn(numberList, index)
        if resultList is not None:
            return resultList


def verifyNumbers(numbers):
    for index, num in enumerate(numbers):
        if index < 25:
            continue
        myScope = getCurrentScope(index)
        isValid = isCurrentNumberValid(num, myScope)
        if not isValid:
            return num


if __name__ == '__main__':
    numbers = parseData("input")
    result = verifyNumbers(numbers)
    print(result)

    mySet = findContiguousSet(numbers)
    print(mySet)
    resultPartTwo = min(mySet) + max(mySet)
    print(resultPartTwo)
