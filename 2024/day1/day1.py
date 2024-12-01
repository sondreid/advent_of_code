


def read_data(file_path: str) -> tuple[list[int], list[int]]:
    list1 = []
    list2 = []
    with open(file_path, 'r') as file:
        for line in file:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)
    return list1, list2


def calculate_absolutes_of_list(list1 : list[int], list2 : list[int]) -> list[int]:

    list1 = sorted(list1)
    list2 = sorted(list2)
    return [abs(num1 - num2) for num1, num2 in zip(list1, list2)]





if __name__ == "__main__":

    list1, list2 = read_data('data.txt')
    print(list1)
    print(list2)
    print(sum(calculate_absolutes_of_list(list1, list2)))
    print("hei")