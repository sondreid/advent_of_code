
# import numpy as np
from typing import List
import re


class calculateCombination():

    def __init__(self) -> None:
        self.num_dict: dict[str, str] = {'one': '1', 'two': '2', 'three': '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight': '8', 'nine' : '9'}

    def find_integer_regex(self, text: str, regex_expression='\d') -> List:
        return re.findall(regex_expression, text)

    def convert_to_integers(self, text: str) -> str:

        for key, value in  self.num_dict.items():
            text = text.replace(key, value)
        return text


    def parse_all_numbers(self, combination):
        
        possible_numbers = ""
        for i in range(0, len(combination)):
            if combination[i].isdigit():
                possible_numbers += combination[i]
                continue

            for j in range(i, len(combination)):
                possible_numbers += self.convert_to_integers(combination[i:j])

        return possible_numbers


    def read_combination(self, combination: str) -> int:

        combination_parsed = self.parse_all_numbers(combination)
        integers = self.find_integer_regex(text=combination_parsed)
        if len(integers) == 0:
            return 0
        return integers[0] + integers[-1]
    




class SuperTextReader():

    def __init__(self, file_name: str) -> None:
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
    combiner = calculateCombination()
    sum = 0
    for i in range(0, supertextreader.num_lines()):

        combination = supertextreader.read_line(i)
        sum += int(combiner.read_combination(combination))
    print(f"Total sum {sum}")

    # print(find_integer_regex("1gregre3"))
