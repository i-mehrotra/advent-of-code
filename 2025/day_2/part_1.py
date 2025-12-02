from typing import List, Union


def parse_input(path: str) -> List[List[Union[str, int]]]:
    ranges: List[List[int]] = []

    with open(path, "r") as file:
        for line in file:
            items = line.split(',')
            for item in items:
                range: List[int] = []
                index = item.index('-')
                range.append(int(item[0:index]))
                range.append(int(item[index+1:]))
                ranges.append(range)
    return ranges

def solve(ids: List[int]) -> int:
    invalid_ids: List[int] = []
    for id in range(ids[0], ids[1] + 1):
        if len(str(id)) % 2 != 0:
            continue
        
        half_index = int(len(str(id)) / 2)
        if str(id)[0:half_index] == str(id)[half_index:]:
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