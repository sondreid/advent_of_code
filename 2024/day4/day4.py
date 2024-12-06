"""This is a word search puzzle where we need to:

1. Read a grid of letters from the input
2. Find all occurrences of the word "XMAS" in the grid
3. The word can appear:
    - Horizontally
    - Vertically 
    - Diagonally
    - Backwards
    - Overlapping with other instances
4. Count the total number of times "XMAS" appears

The key challenge is implementing a search algorithm that can check all possible directions and handle overlapping matches while scanning through the grid.

Let me know when you'd like me to provide code to solve this puzzle.

"""

import os

def is_xmas(candidate: str) -> bool:
    return candidate == "XMAS"



def read_data() -> str:
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, 'data.txt')
    with open(data_path) as f:
        data = f.readlines()
        return data

def check_horizontal(row: str, index : str) -> int:

    counter = 0
    if index -4 > 0:
        print(row[index-4:index])
        if is_xmas(row[index-4:index]):
            counter +=1
        
    if index +4 <= len(row):
        
        if is_xmas(row[index:index+4]):
            counter +=1
    return counter


def check_diagonal(grid, i, j) -> int:

    counter = 0


    northwest_direction = "".join([grid[i-k][j-k] for k in range(0, 4) if i-k >= 0 and j-k >= 0])
    north_direction = "".join([grid[min(i-k,0)][j] for k in range(0, 4)])
    return northwest_direction

def iterate_over_grid(grid: list[str]) -> int:

    counter = 0
    for i in range(0, len(grid)):
        row = grid[i]
        for j in range(0, len(row)):
            horizontal_counter = check_horizontal(row, j)
            #diagonal_counter = check_diagonal(grid, i, j)
            counter = counter + horizontal_counter# + diagonal_counter
    return counter
if __name__ == "__main__":
    
    data = read_data()
    #print(data)
    TEST_GRID = "XMASXXMASSAMX" 
    TEST_GRID2= [
"MMMSXXMASM",
"MSAMXMSMSA",
"AMXSXMAAMM",
"MSAMASMSMX",
"XMASAMXAMM",
"XXAMMXXAMA",
"SMSMSASXSS",
"SAXAMASAAA",
"MAMMMXMMMM",
"MXMXAXMASX"]
    print(check_horizontal(TEST_GRID, 9))
    print(check_diagonal(TEST_GRID2, 3, 0))

