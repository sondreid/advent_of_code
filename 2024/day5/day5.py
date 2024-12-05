




def load_data(filename) -> (list[str], list[str]):
   with open(filename) as f:
        data = f.readlines()
        without_line_breaks = list(map(lambda x: x.split('\n')[0], data))

        data_seperation = without_line_breaks.index("")
        return without_line_breaks[0:data_seperation], without_line_breaks[data_seperation+1:]
    


def loop_through_rule(rules : str, pages : str)

if __name__ == "__main__":
    rules, pages = load_data("data.txt")
    pages: str = ",".join(pages)

        