import re
from copy import deepcopy
from typing import List

from file_opener import getInputFileLinesAsList


class Task:

    def __init__(self):
        self.isVisited = False

    def execute(self, state: dict):
        pass


class NOPTask(Task):

    def __init__(self, valueOffset, isVisited=False):
        super().__init__()
        self.valueOffset = valueOffset
        self.isVisited = isVisited

    def execute(self, state: dict):
        # print('nop ', self.valueOffset)
        state.update({'pointer': state.get('pointer') + 1})
        self.isVisited = True


class AccTask(Task):

    def __init__(self, valueOffset, isVisited=False):
        super().__init__()
        self.valueOffset = valueOffset
        self.isVisited = isVisited

    def execute(self, state: dict):
        # print('acc ', self.valueOffset)
        state.update({'pointer': state.get('pointer') + 1})
        state.update({'value': state.get('value') + self.valueOffset})
        self.isVisited = True


class JmpTask(Task):

    def __init__(self, pointerOffset, isVisited=False):
        super().__init__()
        self.pointerOffset = pointerOffset
        self.isVisited = isVisited

    def execute(self, state: dict):
        # print('jmp ', self.pointerOffset)
        state.update({'pointer': state.get('pointer') + self.pointerOffset})
        self.isVisited = True


def parseInput():
    taskInput = getInputFileLinesAsList("src/part_one/day_1/input")
    pattern = re.compile(r"(?P<task>[a-z]{3}) (?P<number>[+|-]\d+)")
    taskList = []
    for line in taskInput:
        matcher = pattern.match(line)
        taskList.append(createTaskObject(matcher.group("task"), int(matcher.group("number"))))
    return taskList


def createTaskObject(taskType: str, number: int):
    if taskType == "nop":
        return NOPTask(number)
    elif taskType == "acc":
        return AccTask(number)
    elif taskType == "jmp":
        return JmpTask(number)


def iterateThroughTasks(taskList: List[Task]):
    state = {'pointer': 0, 'value': 0}

    while taskList[state.get('pointer')].isVisited is not True:
        taskList[state.get('pointer')].execute(state)
        if state.get('pointer') == len(taskList):
            return state

    print('state: ', state)
    return state


def switchTaskType(task, index, taskList):
    print("switching ", task.__class__, " index: ", index)
    if isinstance(task, NOPTask):
        taskList[index] = JmpTask(task.valueOffset)
    elif isinstance(task, JmpTask):
        taskList[index] = NOPTask(task.pointerOffset)


def searchForWrongTask(taskList: List[Task]):
    for index, task in enumerate(taskList):
        if couldTaskBeWrong(task):
            copy = deepcopy(taskList)
            switchTaskType(task, index, copy)
            myState = iterateThroughTasks(copy)
            if myState.get('pointer') == len(taskList):
                return myState


def couldTaskBeWrong(task: Task):
    return isinstance(task, NOPTask) or isinstance(task, JmpTask)


if __name__ == '__main__':
    taskList = parseInput()
    taskListCopy = deepcopy(taskList)
    iterateThroughTasks(taskList)

    print(searchForWrongTask(taskListCopy))
