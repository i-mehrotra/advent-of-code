from typing import Dict, List, Tuple, Union

def parse_input(path: str) -> List[List[Union[str, int]]]:
    combo: List[List[Union[str, int]]] = []

    with open(path, "r") as file:
        for line in file:
            step: List[Union[str, int]] = []
            step.append(line[0])
            step.append(int(line[1:]))
            combo.append(step)
    return combo

def calculate_step(start: int, step: List[Union[str, int]]) -> Tuple[int, int]:
    rotations = step[1] // 100
    count = rotations
    step[1] -= (100 * rotations)

    if step[0] == 'R':
        stop = start + step[1]
        
    elif step[0] == 'L':
        stop = start - step[1]

    if (stop < 1 or stop > 99) and start != 0:
        count += 1

    stop %= 100
    return stop, count
        
combo = parse_input("/Users/isabellamehrotra/Documents/advent-of-code/2025/day_1/input.txt")
total_count = 0
start = 50
for step in combo:
    start, count = calculate_step(start, step)
    total_count += count
print(total_count)