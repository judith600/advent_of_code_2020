import sys
sys.path.append('/workspace/advent_of_code_2020/advent/2019/src')
import file_opener


if __name__ == "__main__":
    for elem in sys.path:
        print(elem)
    file = file_opener.FileOpener()
    file.openInputFile(2019, 'input.txt')