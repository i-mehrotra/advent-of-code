from hashlib import new
from typing import List

def track_guard(path: str) -> int:
    obstacles = 0
    
    with open(path, "r") as file:
        map: List[List[str]] = []
        for i, line in enumerate(file):
            line = line[:-1]
            line = list(line)
            if "^" in line:
                guard_row = i
                guard_column = line.index("^")
            map.append(line)
    
    row_count = len(map)
    column_count = len(map[0])

    for i in range(row_count):
        for j in range(column_count):
            new_map = map
            if new_map[i][j] == ".":
                new_map[i][j] = "#"
                obstacles += get_obstacles(map, guard_row, guard_column)
                new_map[i][j] = "."
    return obstacles

def get_obstacles(map: List[List[str]], guard_row: int, guard_column) -> int:
    row_count = len(map)
    column_count = len(map[0])
    visited: List[str] = []
    current_direction = "up"
    condition = True
    while condition:
        if current_direction == "up":
            while map[guard_row - 1][guard_column] != "#":
                if str(guard_row) + "," + str(guard_column) + "," + current_direction in visited:
                    return 1
                visited.append(str(guard_row) + "," + str(guard_column) + "," + current_direction)
                guard_row -= 1
                if guard_row == 0: 
                    condition = False
                    break
            current_direction = "right"

        elif current_direction == "right":
            while map[guard_row][guard_column + 1] != "#":
                if str(guard_row) + "," + str(guard_column) + "," + current_direction in visited:
                    return 1
                visited.append(str(guard_row) + "," + str(guard_column) + "," + current_direction)
                guard_column += 1
                if guard_column == column_count - 1: 
                    condition = False
                    break
            current_direction = "down"

        elif current_direction == "down":
            while map[guard_row + 1][guard_column] != "#":
                if str(guard_row) + "," + str(guard_column) + "," + current_direction in visited:
                    return 1
                visited.append(str(guard_row) + "," + str(guard_column) + "," + current_direction)
                guard_row += 1
                if guard_row == row_count - 1:
                    condition = False
                    break
            current_direction = "left"

        else:
            while map[guard_row][guard_column - 1] != "#":
                if str(guard_row) + "," + str(guard_column) + "," + current_direction in visited:
                    return 1
                visited.append(str(guard_row) + "," + str(guard_column) + "," + current_direction)
                guard_column -= 1
                if guard_column == 0:
                    condition = False
                    break
            current_direction = "up"
    return 0
    
print(track_guard("day_6/input.txt"))