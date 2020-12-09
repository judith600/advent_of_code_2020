from file_opener import *


def checkSum(numbers):
    for firstNumber in numbers:
        for secondNumber in numbers:
            for thirdNumber in numbers:
                if int(firstNumber) + int(secondNumber) + int(thirdNumber) == 2020:
                    return int(firstNumber) * int(secondNumber) * int(thirdNumber)


if __name__ == "__main__":
    numberList = getInputFileLinesAsList("src/part_one/day_1/input")
    rightSum = checkSum(numberList)
    print(rightSum)
