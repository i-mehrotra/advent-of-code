from typing import List

def track_guard(path: str) -> int:
    guard_row = 0
    guard_column = 0
    
    with open(path, "r") as file:
        map: List[List[str]] = []
        for i, line in enumerate(file):
            line = line[:-1]
            line = list(line)
            if "^" in line:
                guard_row = i
                guard_column = line.index("^")
            map.append(line)
    
    return len(get_path(map, guard_row, guard_column)) + 1

def get_path(map: List[List[str]], guard_row: int, guard_column: int) -> List[str]:
    row_count = len(map)
    column_count = len(map[0])

    visited: List[str] = []
    current_direction = "up"
    condition = True
    while condition:
        if current_direction == "up":
            while map[guard_row - 1][guard_column] != "#":
                if str(guard_row) + "," + str(guard_column) not in visited:
                    visited.append(str(guard_row) + "," + str(guard_column))
                guard_row -= 1
                if guard_row == 0: 
                    condition = False
                    break
            current_direction = "right"

        elif current_direction == "right":
            while map[guard_row][guard_column + 1] != "#":
                if str(guard_row) + "," + str(guard_column) not in visited:
                    visited.append(str(guard_row) + "," + str(guard_column))
                guard_column += 1
                if guard_column == column_count - 1: 
                    condition = False
                    break
            current_direction = "down"

        elif current_direction == "down":
            while map[guard_row + 1][guard_column] != "#":
                if str(guard_row) + "," + str(guard_column) not in visited:
                    visited.append(str(guard_row) + "," + str(guard_column))
                guard_row += 1
                if guard_row == row_count - 1:
                    condition = False
                    break
            current_direction = "left"

        else:
            while map[guard_row][guard_column - 1] != "#":
                if str(guard_row) + "," + str(guard_column) not in visited:
                    visited.append(str(guard_row) + "," + str(guard_column))
                guard_column -= 1
                if guard_column == 0:
                    condition = False
                    break
            current_direction = "up"

    return visited
    
print(track_guard("day_6/input.txt"))