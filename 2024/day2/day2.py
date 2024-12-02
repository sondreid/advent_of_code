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

def count_safe_reports(reports, safe_tester = is_safe_report):
    return sum(safe_tester(report) for report in reports)

def brute_force_safe_tester(report):
    for number_index in range(0, len(report)):
        report_copy = report.copy()
        report_copy.pop(number_index)
        if is_safe_report(report_copy):
            return True
    return False
if __name__ == '__main__':
    line_reader = read_lines("data.txt")
    reports = [convert_to_integers(line) for line in line_reader]


    safe_reports = count_safe_reports(reports)
    print(count_safe_reports(reports, brute_force_safe_tester))