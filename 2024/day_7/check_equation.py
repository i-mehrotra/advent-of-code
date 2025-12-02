import itertools
from typing import List, Union

def return_sum(path: str) -> int:
    sum = 0
    with open(path, "r") as file:
        vals: List[Union[int, str]]
        for line in file:
            solution = int(line[:line.index(":")])
            vals = line[line.index(":") + 2:-1].split(" ")
            for i in range(len(vals)):
                vals[i] = int(vals[i])
            for i in range(len(vals) + len(vals) - 2):
                if vals[i] != ".":
                    vals.insert(i + 1, ".")
            equations = get_equations(vals)
            for equation in equations:
                actual = check_equation(equation, solution)
                sum += actual
                print(str(solution) + ": " + str(actual))
                print(sum)
                if actual != 0:
                    break
    return sum

def get_equations(vals: List[int]) -> List:
    equations: List[List[Union[int, str]]] = []
    combinations = operator_combinations("+*", len(vals) - 1)
    
    for combination in combinations:
        copy = vals.copy()
        for j in range(len(vals)):
            if copy[j] == ".":
                copy[j] = combination[j]
                equations.append(copy)
    return equations

def operator_combinations(string: str, length: int):
    yield from itertools.product(*([string] * length)) 

def check_equation(equation: List[Union[int, str]], solution: int) -> int:
    while len(equation) > 1:
        if equation[0] > solution:
            return 0
        if equation[1] == "+":
            equation[1] = equation[0] + equation[2]
            del equation[2]
            del equation[0]
        elif equation[1] == "*":
            equation[1] = equation[0] * equation[2]
            del equation[2]
            del equation[0]
    if equation[0] == solution:
        return solution
    return 0
    
print(return_sum("day_7/input.txt"))