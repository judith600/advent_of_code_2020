from typing import List
import sys

def getInputFileLinesAsListGitPodWorkaround(fileName: str) -> List[str]:
    rootPath = sys.path[0]
    return [line.rstrip('\n') for line in open(rootPath + "/" + fileName)]

def executeTask(task: str, number: int):
    pass

class Task():
    def __init__(self, value):
        self.value = value

    def execute(self):
        dict = {'value': 0, ''}
        pass

class AddTask(Task):

    def __init__(self, number):
        super.__init__(number)

    




if __name__ == "__main__":
    input = getInputFileLinesAsListGitPodWorkaround("test_input")
    print(input)