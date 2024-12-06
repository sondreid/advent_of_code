import pytest
from day4 import check_horizontal, check_diagonal



# Test data
TEST_GRID = "XMASXXMASSAMX" 


TEST_GRID2= ["MMMSXXMASM",
"MSAMXMSMSA",
"AMXSXMAAMM",
"MSAMASMSMX",
"XMASAMXAMM",
"XXAMMXXAMA",
"SMSMSASXSS",
"SAXAMASAAA",
"MAMMMXMMMM",
"MXMXAXMASX"]
def test_check_horizontal_forward():
    count = check_horizontal(TEST_GRID, 0)
    assert count == 1

def test_check_horizontal_backward():
    count = check_horizontal(TEST_GRID, 9)
    assert count == 1

def test_check_horizontal_no_match():
    count = check_horizontal(TEST_GRID, 6)
    assert count == 0

def test_check_diagonal_forward():
    count = check_diagonal(TEST_GRID2, 0, 0)
    assert count == 0

def test_check_diagonal_backward():
    count = check_diagonal(TEST_GRID2, 9, 9) 
    assert count == 0

def test_check_diagonal_match():
    count = check_diagonal(TEST_GRID2, 4, 4)
    assert count == 1

def test_check_diagonal_multiple():
    count = check_diagonal(TEST_GRID2, 5, 5)
    assert count == 2
