from itertools import groupby
from typing import List

from file_opener import getInputFileLinesAsList


def parseAnswers():
    answers = getInputFileLinesAsList("input.txt")
    answersGrouped = []
    for k, v in groupby(answers, lambda x: x != ''):
        if k:
            answersGrouped.append(list(v))
    return answersGrouped


def countUniqueQuestionsPerGroup(answers: List[List[str]]):
    counter = 0
    for group in answers:
        singleAnswerString = ''.join(group)
        counter += len(set(singleAnswerString))
    return counter


def forEachGroup(answers: List[List[str]]):
    counter = 0
    for group in answers:
        counter += findYesAnsweredQuestionsInGroup(group)
    return counter


def findYesAnsweredQuestionsInGroup(group: List[str]) -> int:
    setGroup = [set(elem) for elem in group]
    if len(setGroup) == 1:
        return len(setGroup[0])
    result = setGroup[0] & setGroup[1]
    for index, elem in enumerate(setGroup[:-1]):
        result = result & elem & setGroup[index + 1]
    return len(result)


if __name__ == '__main__':
    answers = parseAnswers()
    print(countUniqueQuestionsPerGroup(answers))
    print(forEachGroup(answers))
