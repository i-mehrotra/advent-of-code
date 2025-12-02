from typing import List
import re

def multiply(path: str):
    addends: List[int] = []
    sum = 0
    with open(path, "r") as file:
        content = file.read()
        pattern = re.compile("mul\(\d+\,\d+\)")
        matches = pattern.findall(content)

    for item in matches:
        first_digit = item[item.index("(") + 1:item.index(",")]
        second_digit = item[item.index(",") + 1:item.index(")")]
        addends.append(int(first_digit) * int(second_digit))
    
    for item in addends:
        sum += item
    return sum

print(multiply("day_3/input.txt"))