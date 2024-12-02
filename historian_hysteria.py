from typing import List

def get_sorted_lists(path:str):
    left: List[int] = []
    right: List[int] = []

    with open(path, "r") as file:
        for line in file:
            items = line.split("   ") 
            left.append(int(items[0]))
            right.append(int(items[1]))
    
    left = sorted(left)
    right = sorted(right)

    return left, right

def get_distance(left: List[int], right: List[int]) -> int:
    diff: List[int] = []
    sum = 0

    for i in range(len(left)):
        diff.append(abs(left[i] - right[i]))
    
    for i in range(len(diff)):
        sum += diff[i]

    return sum

def get_similarity(left: List[int], right: List[int]) -> int:
    sim: List[int] = []
    sum = 0

    for i in range(len(left)):
        count = right.count(left[i])
        sim.append(count * left[i])
    
    for i in range(len(sim)):
        sum += sim[i]

    return sum
    
x, y = get_sorted_lists("Day 1/input.txt")
print(get_distance(x, y))
print(get_similarity(x, y))