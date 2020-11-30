from file_opener import *


class DayMyDay:

    def __init__(self):
        self.wella = 'wella'

    def test(self):
        print('Made my day!!!', self.wella)
        print(getInputFileLinesAsList('input_michel.txt'))
        print(getInputFileLinesAsString('input_michel.txt'))


if __name__ == "__main__":
    myDay = DayMyDay()
    myDay.test()
