
import os



def load_data(filename) -> tuple[list[str], list[str]]:
   with open(filename) as f:
        data = f.readlines()
        without_line_breaks = list(map(lambda x: x.split('\n')[0], data))

        data_seperation = without_line_breaks.index("")
        return without_line_breaks[0:data_seperation], without_line_breaks[data_seperation+1:]
    


def get_rule_dict(rules_list: list[str]) -> dict[str, str]:
    rules = {}
    for rule in rules_list:
        key, value = rule.split("|")
        if rules.get(key) != None:
            rule_key = rules.get(key)
            rules[key] = rule_key + [value]
        else: rules[key] = [value]
    return rules
    
def break_rule(update, page, rule_dict):
    
    page_index = page.index(update)
    rule_lookup = rule_dict.get(update) if  rule_dict.get(update) != None else []
    for rule in rule_lookup:
        rule_index = page.index(rule) if rule in page else 10000
        if page_index > rule_index:
            return False
    return True

def verify_page(page, rule_dict) -> bool:

    return all([break_rule(update, page, rule_dict) for update in page])


def verify_pages(pages, rule_dict) -> list[list]:

    return [page for page in pages if verify_page(page, rule_dict)]


def sum_correct_pages(correct_pages) -> int:
    return sum(int(page[len(page)//2]) for page in correct_pages)



if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "test_data.txt")
    rules, pages = load_data(data_path)

    rule_dict = get_rule_dict(rules)
    
    
    pages = [page.split(",") for page in pages]
    correct_pages = verify_pages(pages, rule_dict)
    print(sum_correct_pages(correct_pages))


    # Part1
    data_path = os.path.join(current_dir, "data.txt")
    rules, pages = load_data(data_path)

    rule_dict = get_rule_dict(rules)
    
    
    pages = [page.split(",") for page in pages]
    correct_pages = verify_pages(pages, rule_dict)
    print(sum_correct_pages(correct_pages))