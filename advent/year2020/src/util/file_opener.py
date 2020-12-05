from typing import List


def getInputFileLinesAsList(fileName: str) -> List[str]:
    return [line.rstrip('\n') for line in open(fileName)]


def getInputFileLinesAsString(fileName: str) -> str:
    return open(fileName).read()


def readFileInput(fileName: str) -> list:
    file = open(fileName)
    inputList: List[str] = file.readlines()
    inputListConverted: list = []
    for elem in inputList:
        elemNoLineBreak: str = elem.replace("\n", "")
        if elemNoLineBreak.isdigit():
            inputListConverted.append(int(elemNoLineBreak))
    return inputListConverted
