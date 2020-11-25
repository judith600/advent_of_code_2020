import sys
sys.path.append('/workspace/advent_of_code_2020/advent/2019/src')
import file_opener
from ErisType import State

class MatrixBuilder():

    def __init__(self):
        self.matrix = [['+' for x in range (5)] for k in range(5)]

    def fillInitialMatrix(self):
        pass


if __name__ == "__main__":
    builder = MatrixBuilder()
    for line in builder.matrix:
        for col in line:
            print(col)