from typing import List

def parse_input(path: str) -> List[List[str]]:
    grid: List[List[str]] = []
    with open(path, "r") as file:
        for line in file:
            row: List[str] = list(line.strip())
            grid.append(row)
    return grid

def search_grid(grid: List[List[str]]) -> int:
    num_rows = len(grid)
    num_columns = len(grid[0])
    rolls_removed = 0
    
    for i in range(num_rows):
        for j in range(num_columns):
            if grid[i][j] != '@':
                continue
            
            adjacent_count = 0
            # N
            if j > 0:
                if grid[i][j - 1] == '@':
                    adjacent_count += 1
            # S
            if j < num_rows - 1:
                if grid[i][j + 1] == '@':
                    adjacent_count += 1
            # E
            if i < num_columns - 1:
                if grid[i + 1][j] == '@':
                    adjacent_count += 1
            # W
            if i > 0:
                if grid[i - 1][j] == '@':
                    adjacent_count += 1
            # NE
            if j > 0 and i < num_columns - 1:
                if grid[i + 1][j - 1] == '@':
                    adjacent_count += 1
            # NW
            if j > 0 and i > 0:
                if grid[i - 1][j - 1] == '@':
                    adjacent_count += 1
            # SE
            if j < num_rows - 1 and i < num_columns - 1:
                if grid[i + 1][j + 1] == '@':
                    adjacent_count += 1
            # SW
            if j < num_rows - 1 and i > 0:
                if grid[i - 1][j + 1] == '@':
                    adjacent_count += 1
            
            if adjacent_count < 4:
                rolls_removed += 1

    return rolls_removed
            
grid = parse_input("/Users/isabellamehrotra/Documents/advent-of-code/2025/day_4/input.txt")
print(search_grid(grid))