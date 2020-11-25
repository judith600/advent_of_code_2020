import os

class FileOpener:
    
    def openInputFile(self, year: int, fileName: str):
        basePath = './advent'
        year = str(year)
        resources = 'resources'
        path = os.path.join(basePath, year, resources, fileName)
        return open(path)
    
    def readFileInput(self, file) -> list:
        inputList: list[str] = file.readlines()
        inputListConverted: list = []
        for elem in inputList:
            elemNoLineBreak: str = elem.replace("\n", "")
            if elemNoLineBreak.isdigit():
                inputListConverted.append(int(elemNoLineBreak))
        return inputListConverted