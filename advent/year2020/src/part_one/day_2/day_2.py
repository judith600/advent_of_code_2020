from file_opener import *


def isValid(minimum, maximum, letter, password):
    count = password.count(letter)
    if minimum <= count <= maximum:
        return True
    return False


def isValidXOR(posOne, posTwo, letter, password):
    charOne = password[posOne - 1]
    charTwo = password[posTwo - 1]
    return bool(charOne == letter) ^ bool(charTwo == letter)


def countValidPasswords(passwordList: List[str]):
    countValid = 0
    for line in passwordList:
        lineNew = line.replace(':', '')
        parameter = lineNew.split(' ')
        validRange = parameter[0].split('-')
        result = isValid(int(validRange[0]), int(validRange[1]), parameter[1], parameter[2])
        if result:
            countValid += 1
    return countValid


def countValidPasswordsPartTwo(passwordList: List[str]):
    countValid = 0
    for line in passwordList:
        lineNew = line.replace(':', '')
        parameter = lineNew.split(' ')
        validRange = parameter[0].split('-')
        result = isValidXOR(int(validRange[0]), int(validRange[1]), parameter[1], parameter[2])
        if result:
            countValid += 1
    return countValid


if __name__ == "__main__":
    fileInput = getInputFileLinesAsList("src/part_one/day_2/day_2_input.txt")
    print(countValidPasswords(fileInput))
    print(countValidPasswordsPartTwo(fileInput))
