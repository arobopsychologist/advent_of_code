from collections import Counter

from advent_of_code.utils import file_to_lines


def _get_data():
    lines = file_to_lines("data/2024/day_01.data")

    left_values = []
    right_values = []

    for line in lines:
        left, right = line.split("   ")
        left_values.append(int(left))
        right_values.append(int(right))

    return left_values, right_values


def problem_1():
    left_values, right_values = _get_data()

    left_values.sort()
    right_values.sort()

    difference = 0

    for left, right in zip(left_values, right_values):
        difference += abs(left - right)

    return difference


def problem_2():
    left_values, right_values = _get_data()

    occurences = Counter(right_values)

    similarity_score = 0

    for value in left_values:
        similarity_score += value * occurences[value]

    return similarity_score


if __name__ == "__main__":
    print(problem_1())
    print(problem_2())
