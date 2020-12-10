from day_9 import getInputNumerical

differenceDict = {'one': 0, 'two': 0, 'three': 0}
differenceList = []


def countJoltageDifferences(numberList):
    it = iter(numberList)
    currentNum = 0

    while True:
        try:
            nextNum = next(it)
            difference = nextNum - currentNum
            appendDifference(difference)
            currentNum = nextNum
        except StopIteration:
            print('End of List')
            differenceDict['three'] = differenceDict.get('three') + 1
            differenceList.append(3)
            return differenceDict


def appendDifference(diff):
    differenceList.append(diff)


def fillDifferenceDict(diff):
    if diff == 1:
        differenceDict['one'] = differenceDict.get('one') + 1
    elif diff == 2:
        differenceDict['two'] = differenceDict.get('two') + 1
    elif diff == 3:
        differenceDict['three'] = differenceDict.get('three') + 1
    else:
        raise ValueError('Difference is bigger than 3!!')


def findEnclosedElements(myList):
    indicesOfEnclosedELements = []
    for index, elem in enumerate(myList):
        if index == len(myList) - 1:
            continue
        if myList[index] == 1 and myList[index + 1] == 1:
            indicesOfEnclosedELements.append(index)
    return indicesOfEnclosedELements


if __name__ == '__main__':
    adapterList = getInputNumerical("test_input")
    adapterList.sort()
    resultOne = countJoltageDifferences(adapterList)
    # print(resultOne)
    # print(differenceDict.get('one') * differenceDict.get('three'))

    print(len(adapterList), '            numbers: ', adapterList)
    print(len(differenceList), 'diff to predecessor: ', differenceList)
    enclosedIndices = findEnclosedElements(differenceList)
    print(enclosedIndices)

    elementsCanBeLeftOut = [adapterList[index] for index in enclosedIndices]
    print(len(elementsCanBeLeftOut), elementsCanBeLeftOut)

