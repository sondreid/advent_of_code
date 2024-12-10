import os


def load_data(filename) -> tuple[list[str], list[str]]:
    with open(filename) as f:
        data = f.readlines()
        without_line_breaks = list(map(lambda x: x.split("\n")[0], data))

        data_seperation = without_line_breaks.index("")
        return (
            without_line_breaks[0:data_seperation],
            without_line_breaks[data_seperation + 1 :],
        )


def get_rule_dict(rules_list: list[str]) -> dict[str, str]:
    rules = {}
    for rule in rules_list:
        key, value = rule.split("|")
        if rules.get(key) != None:
            rule_key = rules.get(key)
            rules[key] = rule_key + [value]
        else:
            rules[key] = [value]
    return rules


def verify_update(update, page, rule_dict):

    page_index = page.index(update)
    rule_lookup = rule_dict.get(update) if rule_dict.get(update) != None else []
    for rule in rule_lookup:
        rule_index = page.index(rule) if rule in page else 10000
        if page_index > rule_index:
            return False
    return True


def verify_page(page, rule_dict) -> bool:
    return all([verify_update(update, page, rule_dict) for update in page])


def verify_pages(pages, rule_dict) -> list[list]:
    return [page for page in pages if verify_page(page, rule_dict)]


def sum_middle_numbers(correct_pages) -> int:
    return sum(int(page[len(page) // 2]) for page in correct_pages)



def sort_page(rule_dict: dict, page) -> list[str]:


    rule_dict_cp  = { k: rule_dict[k] for k in rule_dict.keys() if  k in page}
    
    keys = [ key for key, values in rule_dict_cp.items() if key in page]
    rule_values = sum(rule_dict_cp.values(), [])

    # Find intitial candidates

    sorted_page = []
    for key in keys:
        if key not in rule_values:
            candidate_values = [x for x in rule_dict_cp.get(key) if x in page ]
            sorted_page.append(key)
            del rule_dict_cp[key]
            break
    if candidate_values == None:
        return

    while len(candidate_values) > 0:
        if len(page) == len(sorted_page):
                return sorted_page
        rule_values = sum(rule_dict_cp.values(), [])

        if len(rule_dict_cp) == 1:
            key = [ key for key, values in rule_dict_cp.items() if key in page]
            if key[0] in page:
                sorted_page.append(key[0])
                values =  [value for value in rule_dict_cp.values() if value in page]
                sorted_page = sorted_page + values
                return sorted_page
        for value in candidate_values:
            if value not in rule_values:
                candidate_values = [x for x in rule_dict_cp.get(value) if x in page ]
                if value not in sorted_page:
                    sorted_page.append(value)
                del rule_dict_cp[value]
                break
    return sorted_page



if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "test_data.txt")
    rules, pages = load_data(data_path)

    rule_dict = get_rule_dict(rules)

    pages = [page.split(",") for page in pages]
    correct_pages = verify_pages(pages, rule_dict)
    # print(sum_correct_pages(correct_pages))

    # Part1
    data_path = os.path.join(current_dir, "data.txt")
    rules, pages = load_data(data_path)

    rule_dict = get_rule_dict(rules)

    pages = [page.split(",") for page in pages]
    correct_pages = verify_pages(pages, rule_dict)
    print(sum_middle_numbers(correct_pages))

    # Part 2
    data_path = os.path.join(current_dir, "data.txt")
    rules, pages = load_data(data_path)
    rule_dict = get_rule_dict(rules)
    pages = [page.split(",") for page in pages]



    incorrect_pages  = [page for page in pages if not verify_page(page, rule_dict)]

    reordered_incorrect_pages = [sort_page(rule_dict, page) for page in incorrect_pages]
    #print(reordered_incorrect_pages)
    print(sum_middle_numbers(reordered_incorrect_pages))

