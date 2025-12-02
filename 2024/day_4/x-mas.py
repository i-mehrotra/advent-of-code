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
    
    for i in range(1, row_count - 1):
        for j in range(1, column_count - 1):
            if arr[i][j] == "A":
                # NW and SE
                if (arr[i-1][j-1] == "M" and arr[i+1][j+1] == "S") or (arr[i-1][j-1] == "S" and arr[i+1][j+1] == "M"):
                    # NE and SW
                    if (arr[i-1][j+1] == "M" and arr[i+1][j-1] == "S") or (arr[i-1][j+1] == "S" and arr[i+1][j-1] == "M"):
                        count += 1
    return count
    
print(word_search("day_4/input.txt"))