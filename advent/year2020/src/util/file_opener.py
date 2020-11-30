from typing import List


def getInputFileLinesAsList(fileName: str) -> List[str]:
    return open(fileName).readlines()


def getInputFileLinesAsString(fileName: str) -> str:
    return open(fileName).read()


def readFileInput(file) -> list:
    inputList: List[str] = file.readlines()
    inputListConverted: list = []
    for elem in inputList:
        elemNoLineBreak: str = elem.replace("\n", "")
        if elemNoLineBreak.isdigit():
            inputListConverted.append(int(elemNoLineBreak))
    return inputListConverted
