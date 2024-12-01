import pytest
import day2


text_reader = day2.SuperTextReader('test.txt')
first_line = text_reader.read_line(0)


def assert_true():
    assert True



def assert_red_count():

    valid_game = day2.ValidGameDeterimnator()
    assert valid_game.count_colors('red', first_line)


def assert_game_id_count():

    valid_game = day2.ValidGameDeterimnator()
    assert valid_game.get_game_id(first_line) == 1


def assert_sum_of_game_ids():

    valid_game = day2.ValidGameDeterimnator()
    sum = 0
    for i in range(0, text_reader.num_lines()):
        game_line  = text_reader.read_line(i)
        sum += valid_game.return_game_sum(game_line)

    
    assert sum == 10

assert_red_count()
assert_game_id_count()
assert_sum_of_game_ids()