from typing import List

def parse_input(path: str) -> List[str]:
    banks: List[str] = []
    with open(path, "r") as file:
        for line in file:
            banks.append(line.strip())
    return banks

def get_highest_joltage(batteries: List[str], iter: int):
    highest = int(batteries[0])
    index = 0
    for i in range(1, len(batteries)):
        if int(batteries[i]) > highest and len(batteries) - i >= 12 - iter:
            highest = int(batteries[i])
            index = i
    return highest, index

banks = parse_input("/Users/isabellamehrotra/Documents/advent-of-code/2025/day_3/input.txt")
highest_jolts: List[int] = []
for batteries in banks:
    num_str = ""
    for iter in range(12):
        highest, i = get_highest_joltage(batteries, iter)
        num_str += str(highest)
        batteries = batteries[i+1:]
    highest_jolts.append(int(num_str))

sum = 0
for jolts in highest_jolts:
    sum += jolts
print(sum)