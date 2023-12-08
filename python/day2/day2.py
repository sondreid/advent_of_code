


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

class ValidGameDeterimnator():


    cube_counts: dict[str, int] = {'red' : 12, 'green': 13, 'blue': 14}


    def __init__(self) -> None:
        pass




    def count_colors(self, color : str, game_line : str) -> bool:


        game_draws = game_line.split(':')[-1]
        # strip white space
        game_draws = game_draws.strip(' ')
        counts_color = len(game_draws.split(color))

        # Loop through all instances of count
        for i in range(0, counts_color):
            #print(f"game_line  {game_draws.split(color)[i].strip(' ')}")
            try:
                color_count = game_draws.split(color)[i].strip(' ')[-1] # Last
            except:
                continue
            if color_count.isdigit():
                print(color_count)
                if int(color_count) > self.cube_counts[color]:
                    return False
        return True
    
    def return_game_sum(self, game_line : str):

        for color, count in self.cube_counts.items():
            if not self.count_colors(color, game_line):
                return 0
        return self.get_game_id(game_line)

    

    def get_game_id(self, game_line : str) -> int:
        
        try:
            game_id = int(game_line.split(':')[0].strip(' ')[-1])

            return game_id
        except:
            return 0
        


        
if __name__ == '__main__':
    text_reader =SuperTextReader('data.txt')
    valid_game = ValidGameDeterimnator()
    sum = 0
    for i in range(0, text_reader.num_lines()):
        game_line  = text_reader.read_line(i)
        sum += valid_game.return_game_sum(game_line)
    print(sum)
