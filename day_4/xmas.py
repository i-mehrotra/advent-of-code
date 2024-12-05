from typing import List

def word_search(path: str) -> int:
    count = 0
    with open(path, "r") as file:
        arr: List[List[str]] = []
        for line in file:
            line = line[:-1]
            line = list(line)
            arr.append(line)
    
    row_count = len(arr)
    column_count = len(arr[0])
    
    count += check_E_and_W(arr, row_count, column_count)
    count += check_N_and_S(arr, row_count, column_count)
    count += check_SE(arr, row_count, column_count)
    count += check_SW(arr, row_count, column_count)

    return count
    
def check_E_and_W(arr: List[List[str]], row_count: int, column_count: int) -> int:
    count = 0
    for i in range(row_count):
        for j in range(0, column_count - 3):
            if arr[i][j] == "X":
                if arr[i][j+1] == "M":
                    if arr[i][j+2] == "A":
                        if arr[i][j+3] == "S":
                            count += 1
            elif arr[i][j] == "S":
                if arr[i][j+1] == "A":
                    if arr[i][j+2] == "M":
                        if arr[i][j+3] == "X":
                            count += 1
    return count

def check_N_and_S(arr: List[List[str]], row_count: int, column_count: int) -> int:
    count = 0
    for i in range(0, row_count - 3):
        for j in range(column_count):
            if arr[i][j] == "X":
                if arr[i+1][j] == "M":
                    if arr[i+2][j] == "A":
                        if arr[i+3][j] == "S":
                            count += 1
            elif arr[i][j] == "S":
                if arr[i+1][j] == "A":
                    if arr[i+2][j] == "M":
                        if arr[i+3][j] == "X":
                            count += 1
    return count

def check_SE(arr: List[List[str]], row_count: int, column_count: int) -> int:
    count = 0
    for i in range(0, row_count - 3):
        for j in range(0, column_count - 3):
            if arr[i][j] == "X":
                if arr[i+1][j+1] == "M":
                    if arr[i+2][j+2] == "A":
                        if arr[i+3][j+3] == "S":
                            count += 1
            elif arr[i][j] == "S":
                if arr[i+1][j+1] == "A":
                    if arr[i+2][j+2] == "M":
                        if arr[i+3][j+3] == "X":
                            count += 1
    return count

def check_SW(arr: List[List[str]], row_count: int, column_count: int) -> int:
    count = 0
    for i in range(0, row_count - 3):
        for j in range(3, column_count):
            if arr[i][j] == "X":
                if arr[i+1][j-1] == "M":
                    if arr[i+2][j-2] == "A":
                        if arr[i+3][j-3] == "S":
                            count += 1
            elif arr[i][j] == "S":
                if arr[i+1][j-1] == "A":
                    if arr[i+2][j-2] == "M":
                        if arr[i+3][j-3] == "X":
                            count += 1
    return count

print(word_search("day_4/input.txt"))