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

                results = []
                for i in range(10):
                    x = get_middle(line, rules)
                    if i == 0 and x == 0:
                        sum += 0
                        break
                    else:
                        results.append(x)
                if 0 in results:
                    zero_index = results.index(0)
                    sum += results[zero_index - 1]
    return sum

def get_middle(pages: List[str], rules: Dict) -> int:
    condition: bool = False
    for i in range(len(pages)):
        pages[i] = int(pages[i])
        number = pages[i]
        count = 0
        if number in rules.keys():
            followers = rules.get(number)
            for follower in followers:
                if follower in pages:
                    follower_index = pages.index(follower)
                    if follower_index < i:
                        condition = True
                        pages.pop(follower_index)
                        if count == 0:
                            pages.insert(i, follower)
                        else:
                            pages.insert(pages.index(number) + 1, follower)
                        count += 1
    
    if condition:
        return pages[(int(len(pages) / 2))]
    return 0
    
print(page_orderer("day_5/input.txt"))