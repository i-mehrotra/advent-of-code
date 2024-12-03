from typing import List

def safety_count(path: str) -> int:
    count = 0
    with open(path, "r") as file:
        for line in file:
            report = line.split(" ")
            for i in range(len(report)):
                report[i] = int(report[i])

            error_index = check_safety(report)
            if error_index == -1:
                count += 1
            else:
                # Run check_safety() again on two variations of the list that had a failing interval.
                # One list will have the left failing value removed, the other will have the right failing value removed.
                left_removed = report[:error_index] + report[error_index + 1:]
                right_removed = report[:error_index + 1] + report[error_index + 2:]
                if check_safety(left_removed) == -1 or check_safety(right_removed) == -1:
                    count += 1
    return count

def check_safety(report: List[int]) -> int:
    # Check if a list is "safe." Return -1 if it is safe,
    # return the index of the failing interval if unsafe.
    intervals: List[int] = []
    for i in range(len(report) - 1):
        intervals.append(report[i + 1] - report[i])

    # Determine if the overall trend of the list is increasing or decreasing.
    trend = 0
    for i in intervals:
        if i > 0:
            trend += 1
        if i < 0:
            trend -= 1
    # If there is no obvious trend, arbitrarily select increasing.
    if trend == 0:
        trend = 1

    for i in range(len(report) - 1):
        delta = report[i + 1] - report[i]
        if abs(delta) < 1 or abs(delta) > 3:
            return i
        if trend > 0 and delta < 0:
            return i
        elif trend < 0 and delta > 0:
            return i
    return -1

print(safety_count("Day 2/input.txt"))