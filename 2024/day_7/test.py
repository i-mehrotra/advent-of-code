import itertools


def operator_combinations(string: str, length: int):
    yield from itertools.product(*([string] * length)) 

combinations = operator_combinations("+*", 10)

for c in combinations:
    print(c)