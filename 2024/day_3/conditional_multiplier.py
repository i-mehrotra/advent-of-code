from typing import List
import re

def multiply(path: str):
    outer: List[str] = []
    addends: List[int] = []
    sum = 0
    with open(path, "r") as file:
        content = file.read()
        pattern = re.compile("(mul\(\d+\,\d+\))|(do\(\))|(don't\(\))")
        matches = pattern.findall(content)

    for triple in matches:
        for item in triple:
            if item != "":
                outer.append(item)
    
    for item in outer:
        if item == "don't()":
            if "do()" in outer:
                for i in range(outer.index(item), outer.index("do()")):
                    outer[i] = "" 
            else:
                break
        elif item == "do()":
            outer[outer.index(item)] = ""
        elif item == "":
            continue
        else:
            first_digit = item[item.index("(") + 1:item.index(",")]
            second_digit = item[item.index(",") + 1:item.index(")")]
            addends.append(int(first_digit) * int(second_digit))
    
    for item in addends:
        sum += item
    return sum

print(multiply("day_3/input.txt"))