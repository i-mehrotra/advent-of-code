from typing import List

def parse_input(path: str) -> List[List[str]]:
    ranges: List[List[str]] = []

    with open(path, "r") as file:
        for line in file:
            items = line.split(',')
            for item in items:
                range: List[str] = []
                index = item.index('-')
                range.append(item[0:index])
                range.append(item[index+1:])
                ranges.append(range)
    return ranges

def find_invalid_ids(pattern: str, id: str) -> bool:
    if id.count(pattern) == len(id) / len(pattern):
        return True
    return False

def solve(ids: List[str]) -> int:
    invalid_ids: List[int] = []
    for id in range(int(ids[0]), int(ids[1]) + 1):
        half_index = len(str(id)) / 2
        for i in range(1, int(half_index) + 1):
            if find_invalid_ids(str(id)[0:i], str(id)) and id not in invalid_ids:
                invalid_ids.append(id)
        
    sum = 0
    for i in invalid_ids:
        sum += i
    
    return sum

ranges = parse_input("/Users/isabellamehrotra/Documents/advent-of-code/2025/day_2/input.txt")
sum = 0
for x in ranges:
    sum += solve(x)
print(sum)