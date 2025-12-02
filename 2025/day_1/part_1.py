from typing import Dict, List, Union

def parse_input(path: str) -> List[List[Union[str, int]]]:
    combo: List[List[Union[str, int]]] = []

    with open(path, "r") as file:
        for line in file:
            step: List[Union[str, int]] = []
            step.append(line[0])
            step.append(int(line[1:]))
            combo.append(step)
    return combo

def calculate_step(start: int, step: List[Union[str, int]]) -> int:
    if step[0] == 'R':
        start += step[1]
        
    elif step[0] == 'L':
        start -= step[1]

    start %= 100
    return start
        
combo = parse_input("/Users/isabellamehrotra/Documents/advent-of-code/2025/day_1/input.txt")
count = 0
start = 50
for step in combo:
    start = calculate_step(start, step)
    if start == 0:
        count += 1
print(count)