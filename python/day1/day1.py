
import numpy as np
from typing import List
import re




def find_integer_regex(text : str) -> List:
    return re.findall('\d', text)


def read_combination(combination : str) ->  int:

    integers = find_integer_regex(text=combination)
    if len(integers) == 0:
        return 0
    return integers[0] + integers[-1]


class SuperTextReader():


    def __init__(self, file_name : str) -> None:
        self.file_name = file_name
        self.lines: list[str] = self.read_files()
    

    def num_lines(self) -> int:

        return len(self.lines)


    def read_files(self):
        with open(self.file_name) as file:
            return file.readlines()
        
    def read_line(self, line_num):

        return self.lines[line_num]



if __name__ == '__main__':
    supertextreader = SuperTextReader(f'data.txt')

    sum = 0
    for i in  range(0, supertextreader.num_lines()):

        combination = supertextreader.read_line(i)
        print(combination)
        print(int(read_combination(combination)))
        sum += int(read_combination(combination))
    print(f"Total sum {sum}")

    #print(find_integer_regex("1gregre3"))

 