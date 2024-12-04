import numpy as np

def get_grid(path: str):
    with open(path, "r") as file:
        lines = []
        for line in file:
            line = line[:-1]
            line = list(line)
            lines.append(line)

    word_search(np.array(lines))

def word_search(grid: np.array):
    pass

print(word_search(get_grid("day_4/input.txt")))

