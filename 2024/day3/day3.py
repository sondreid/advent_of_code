import re



def read_data() -> str:
    with open('data.txt') as f:
        data = f.read()
        return data


def extract_mul_instructions(text: str) -> list[str]:
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    return re.findall(pattern, text)


def extract_instructions(text : str) -> list[str]:
    pattern = r"mul\(\d{1,3},\d{1,3}\)|don't|do"
    return re.findall(pattern, text)

def santize_expression(string: str) -> list[int]:
    return [int(string) for string in string.replace("mul(", "").replace(")", "").split(",")]

def is_mull_expression(mul_candidate) -> bool:

    return len(extract_mul_instructions(mul_candidate)) > 1

def multiply_elements(list: list[int]) -> int:
    product = 1
    return [product := product  * a for a in list][-1]


def add_all_elements(list: list[int]) -> int:
    return sum([multiply_elements(element) for element in list])




def exclude_mull_expressions(expressions : list[str] ):

    skip_mul = False
    valid_expressions = []
    for expression in expressions:
        if expression == "don't":
            skip_mul = True
        elif expression == "do":
            skip_mul = False
        elif not skip_mul and "mul" in expression:
            valid_expressions.append(expression)
    
    return [expression for expression  in valid_expressions]




if __name__ == "__main__":

    data = read_data()

    # Part1
    mul_expressions =extract_mul_instructions(data)
    mul_integers = [santize_expression(expression) for expression in mul_expressions]
    print(add_all_elements(mul_integers))

    # Part2
    instructions  = extract_instructions(data)
    mul_expressions = exclude_mull_expressions(instructions)
    mul_integers = [santize_expression(expression) for expression in mul_expressions]
    print(add_all_elements(mul_integers))

