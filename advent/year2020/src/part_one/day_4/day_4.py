import re
from itertools import groupby
from typing import List

from advent.year2020.src.util.file_opener import getInputFileLinesAsList


def parsePassportData(passportData: List[str]):
    parsedPassportData = []
    for line in passportData:
        splitLines = line.split(" ")
        parsedPassportData.extend(splitLines)
    return parsedPassportData


def groupIntoPassports(passPortData: List[str]) -> List[List[str]]:
    allPassports = []
    for k, v in groupby(passPortData, lambda x: x != ''):
        if k:
            allPassports.append(list(v))
    return allPassports


def convertListToDict(listOfLists):
    dictList = []
    for listElem in listOfLists:
        propertyDict = {}
        for elem in listElem:
            keyValueData = elem.split(':')
            propertyDict[keyValueData[0]] = keyValueData[1]
        dictList.append(propertyDict)
    return dictList


def hasAllRequiredPassportProperties(passport: dict):
    requiredProperties = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for prop in requiredProperties:
        if prop not in passport:
            return False
    return True


def getValidPropertiesPassports(passportList):
    return [p for p in passportList if hasAllRequiredPassportProperties(p)]


def countValidPassports(passportDictList) -> int:
    counter = 0
    for passport in passportDictList:
        if hasAllRequiredPassportProperties(passport):
            counter += 1
    return counter


def isPassportValuesValid(passport: dict):
    byr = checkByr(passport.get('byr'))
    eyr = checkEyr(passport.get('eyr'))
    iyr = checkIyr(passport.get('iyr'))
    hgt = checkHgt(passport.get('hgt'))
    hcl = checkHcl(passport.get('hcl'))
    ecl = checkEcl(passport.get('ecl'))
    pid = checkPid(passport.get('pid'))
    result = byr and eyr and iyr and hgt and hcl and ecl and pid
    if not result:
        print("byr: ", byr,  " eyr: ", eyr, " iyr:", iyr, " hgt:", hgt, " hcl: ", hcl, " ecl: ", ecl, " pid: ", pid)
    return result


def checkByr(value: str):
    year = int(value)
    return 1920 <= year <= 2002


def checkIyr(value: str):
    year = int(value)
    return 2010 <= year <= 2020


def checkEyr(value: str):
    year = int(value)
    return 2020 <= year <= 2030


def checkHgt(value: str):
    pattern = re.compile(r"\d+(cm|in)\b")
    if bool(pattern.match(value)):
        if 'cm' in value and 150 <= int(value[:-2]) <= 193:
            return True
        elif 'in' in value and 59 <= int(value[:-2]) <= 76:
            return True
        else:
            return False


def checkHcl(value: str):
    pattern = re.compile(r'#[0-9a-f]{6}\b')
    return bool(pattern.match(value))


def checkEcl(value: str):
    validEclValues = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return value in validEclValues


def checkPid(value: str):
    pattern = re.compile(r"\b\d{9}\b")
    return bool(pattern.match(value))


def getValidValuesPassports(passportDictList):
    return [passport for passport in passportDictList if isPassportValuesValid(passport)]


def getInvalidPropertiesPassports(passportDictList):
    return [passport for passport in passportDictList if not isPassportValuesValid(passport)]


if __name__ == "__main__":
    data = getInputFileLinesAsList("src/part_one/day_4/input.txt")
    # data = getInputFileLinesAsList("invalid.txt")
    # data = getInputFileLinesAsList("valid.txt")

    passportList = groupIntoPassports(parsePassportData(data))
    passportDictList = convertListToDict(passportList)
    validPropertiesPassports = getValidPropertiesPassports(passportDictList)

    assumedValidPassports = getValidValuesPassports(validPropertiesPassports)
    assumedInvalidPassports = getInvalidPropertiesPassports(validPropertiesPassports)

    # for elem in assumedValidPassports:
        # print(elem)

    print(assumedValidPassports.__len__())
