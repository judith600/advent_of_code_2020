import re

from file_opener import getInputFileLinesAsList

pattern = re.compile(r"(?P<number>\d) (?P<color>.+) (?P<bag>bag|bags.)|(?P<nothing>no)")


def parseBagRules(ruleList):
    bagRuleDict = {}
    for line in ruleList:
        keyValuePair = line.split(" bags contain ")
        numberAndBag = {}
        for elem in keyValuePair[1].split(", "):
            matchOrNone = pattern.match(elem)
            if matchOrNone is not None:
                numberAndBag[matchOrNone.group("color")] = matchOrNone.group("number")
        bagRuleDict[keyValuePair[0]] = numberAndBag
    return bagRuleDict


def searchContainersForBag(searchBag: str, bagRuleDict):
    intermediateResult = []
    for k, v in bagRuleDict.items():
        if searchBag in v:
            intermediateResult.append(k)
    return intermediateResult


def removeDuplicateElements(overallResult, intermediateResult):
    duplicateElements = overallResult.intersection(intermediateResult)
    return [elem for elem in intermediateResult if elem not in duplicateElements]


def getAllBagsForBag(searchBag, bagRuleDict):
    overallResult = set()
    bagsToSearch = [searchBag]
    while len(bagsToSearch) > 0:
        for bag in bagsToSearch:
            intermediateResult = searchContainersForBag(bag, bagRuleDict)
            intermediateResult = removeDuplicateElements(overallResult, intermediateResult)
            bagsToSearch.extend(intermediateResult)
            # print("For ", bag, " adding: ", len(intermediateResult), " ", intermediateResult)
            if len(intermediateResult) > 0:
                overallResult.update(intermediateResult)
            bagsToSearch.remove(bag)
            print("searching for ", len(bagsToSearch), " bags")
    return overallResult


if __name__ == '__main__':
    bagDict = parseBagRules(getInputFileLinesAsList("src/part_one/day_1/input"))
    totalResult = getAllBagsForBag('shiny gold', bagDict)
    print(len(totalResult), totalResult)
