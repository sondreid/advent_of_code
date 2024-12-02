def is_safe_report(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

def convert_to_integers(string : str) -> list[int]:
    return [int(x) for x in string.split(" ")]

def count_safe_reports(reports):
    return sum(is_safe_report(report) for report in reports)

if __name__ == '__main__':
    line_reader = read_lines("data.txt")
    reports = [convert_to_integers(line) for line in line_reader]
    print(reports[0])
    print(is_safe_report(reports[0]))
    print(count_safe_reports(reports))