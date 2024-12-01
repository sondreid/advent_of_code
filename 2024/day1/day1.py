from collections import Counter


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



def calculate_similarity_score(list1: list[int], list2: list[int]) -> int:
    counts_list2 = Counter(list2)
    simil_score = 0
    for i in list1:
        simil_score += counts_list2[i]*i

    return simil_score



if __name__ == "__main__":

    list1, list2 = read_data('data.txt')

    
    #Part1 
    print("> Part 1")
    print(sum(calculate_absolutes_of_list(list1, list2)))

    #Part2
    print("> Part 2")
    print(calculate_similarity_score(list1, list2))
