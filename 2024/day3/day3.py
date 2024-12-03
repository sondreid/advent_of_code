import re



def read_data() -> str:
    with open('data.txt') as f:
        data = f.read()
        return data


def extract_mul_instructions(text: str) -> list[str]:
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    return re.findall(pattern, text)



def santize_expression(string: str) -> list[int]:
    return [int(string) for string in string.replace("mul(", "").replace(")", "").split(",")]


def multiply_elements(list: list[int]) -> int:
    product = 1
    return [product := product  * a for a in list][-1]


def add_all_elements(list: list[int]) -> int:
    return sum([multiply_elements(element) for element in list])

if __name__ == "__main__":

    data = read_data()
    mul_expressions =extract_mul_instructions(data)
    mul_integers = [santize_expression(expression) for expression in mul_expressions]
    print(mul_integers)
    print(add_all_elements(mul_integers))
