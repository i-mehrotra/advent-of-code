from ast import Dict
from typing import List

def page_orderer(path: str) -> int:
    sum = 0
    with open(path, "r") as file:
        rules: Dict[int, List[int]] = {}

        for line in file:
            if "|" in line:
                mid_index = line.index("|")
                first = int(line[:mid_index])
                second = int(line[mid_index+1:line.index("\n")])
                if first not in rules.keys():
                    rules[first] = [second]
                else:
                    rules.get(first).append(second)
            elif "," in line:
                line = line.strip("\n").split(",")
                sum += get_middle(line, rules)
    return sum

def get_middle(pages: str, rules: Dict) -> int:
    for i in range(len(pages)):
        pages[i] = int(pages[i])
        number = pages[i]
        if number in rules.keys():
            followers = rules.get(number)
            for follower in followers:
                if follower in pages:
                    follower_index = pages.index(follower)
                    if follower_index < i:
                        return 0
    return pages[(int(len(pages) / 2))]
    
print(page_orderer("day_5/input.txt"))